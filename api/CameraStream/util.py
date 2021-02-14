import threading

import cv2

lock = threading.Lock()
outputFrames = {}


def start_capture(source):
    global outputFrames

    cap = cv2.VideoCapture(source)
    while True:
        ret, outputFrames[source] = cap.read()


def generate(source):
    # grab global references to the output frame and lock variables
    global outputFrames, lock
    # loop over frames from the output stream
    while True:
        # wait until the lock is acquired
        with lock:
            # check if the output frame is available, otherwise skip
            # the iteration of the loop
            if source not in outputFrames or outputFrames[source] is None:
                continue
            # encode the frame in JPEG format
            (flag, encodedImage) = cv2.imencode(".jpg", outputFrames[source])
            # ensure the frame was successfully encoded
            if not flag:
                continue
        # yield the output frame in the byte format
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' +
               bytearray(encodedImage) + b'\r\n')
