"""
Utils class for handling file uploads, time and other miscellaneous tasks.
"""

import os

import ffmpeg_streaming
from ffmpeg_streaming import Formats
from werkzeug.utils import secure_filename

import constants

ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp', 'mp4'}

"""
Verifies for allowed extensions.
"""


def allowed_file(filename):
    return '.' in filename and get_file_extension(filename=filename) in ALLOWED_EXTENSIONS


def get_file_extension(filename):
    return filename.rsplit('.', 1)[1].lower()
"""
Upload file to specific path. For videos, it's /uploads/videos/<news_id>/file.mp4.
For images, it's /uploads/images/<news_id>/image.jpg.
"""


def upload_file(news, file, upload_type):
    if file is None:
        return ''
    if file and allowed_file(filename=file.filename):
        path = 'uploads/{}/{}/'.format(upload_type, news.id)
        filename = secure_filename(file.filename)
        if not os.path.exists(path):
            os.makedirs(path)
        file_path = os.path.join(path, filename)
        file.save(file_path)
        if get_file_extension(filename=file.filename) == 'mp4':
            video = ffmpeg_streaming.input(file_path)
            dash = video.dash(Formats.h264())
            dash.auto_generate_representations()
            video_name_with_ext = '{}.{}'.format(file.filename.rsplit('.', 1)[0], 'mpd')
            dash.output(path + '/{}'.format(video_name_with_ext))
            os.remove(path=file_path)
            return 'https://thewitness.wielabs.com/uploads/{}/{}/{}'.format(upload_type, news.id, video_name_with_ext)
        return 'https://thewitness.wielabs.com/uploads/{}/{}/{}'.format(upload_type, news.id, filename)
    return ''


"""
Get formatted time of current instant. 
Ex. 25 Dec, 2020 • 09:00 AM
"""


def get_formatted_time():
    from datetime import datetime
    timestamp = datetime.now()
    return '{} {}, {} • {}:{} {}'.format(timestamp.strftime("%d"), timestamp.strftime("%b"), timestamp.strftime("%Y"),
                                         timestamp.strftime("%I"), timestamp.strftime("%M"), timestamp.strftime("%p"))


def get_flag_url(region):
    return constants.BASE_FLAG_URL.format(region.lower())
