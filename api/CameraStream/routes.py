import threading

from flask import Blueprint, Response, request

from util import start_capture, generate

stream_bp = Blueprint('stream_bp', __name__)

# Track the capture sources.
captured_sources = []


@stream_bp.route('/source/<source>')
def capture_stream(source):
    camera_ip = request.args.get('camera_ip')
    if camera_ip is None:
        # Format source based on type.
        # If source is a number, typecast it to int.
        # Otherwise, it could be an IP address of camera.
        if source.isdigit():
            formatted_source = int(source)
        else:
            formatted_source = source

        # Check if the source is in captured_sources, If yes, simply show the live stream.
        # Otherwise, invoke a new thread for the new source.
        if formatted_source not in captured_sources:
            captured_sources.append(formatted_source)
            threading.Thread(target=start_capture, args=(formatted_source,), daemon=True).start()
            # Return response in frames.
        return Response(generate(source=formatted_source), mimetype="multipart/x-mixed-replace; boundary=frame")
    else:
        if camera_ip not in captured_sources:
            captured_sources.append(camera_ip)
            threading.Thread(target=start_capture, args=(camera_ip,), daemon=True).start()
        # Return response in frames.
        return Response(generate(source=camera_ip), mimetype="multipart/x-mixed-replace; boundary=frame")

