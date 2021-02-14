# this for file fetching used for uploading files using url
import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename
from main import flask_app as app
from flask import send_from_directory

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


# @app.route('/', methods=['GET', 'POST'])
def upload_file(path, file, type, id):
    # check if the post request has the file part
    if 'file' is None:
        flash('No file part')
        return redirect(request.url)
    # if user does not select file, browser also
    # submit an empty part without filename
    if file.filename == '':
        flash('No selected file')
        return redirect(request.url)
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        if not os.path.exists(path):
            os.makedirs(path)
        file.save(os.path.join(path, filename))
        return 'http://localhost:5000/uploads/{}/{}/{}'.format(type, id, filename)
