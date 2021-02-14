import json
from flask import Flask, request, jsonify
from pymongo import MongoClient, errors
from datetime import datetime
import pytz

with open('config.json', 'r') as read_it:
    urls = json.load(read_it)
    DATABASE_URI = urls['mongo_uri']

app = Flask(__name__)
app.url_map.strict_slashes = False
client = MongoClient(DATABASE_URI)  # host uri
db = client.dummy  # Select the database
postData = db.device_post
getData = db.device_get

IST = pytz.timezone('Asia/Kolkata')


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        req_time = datetime.now(IST)
        req_timestamp = req_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")
        ip_address = request.headers['X-Real-IP']

        getData.insert_one({"method": "GET",
                            "device_ip": ip_address,
                            "request_time": req_timestamp})

        return jsonify({"status": 'Server Online'})

    if request.method == 'POST':
        req_time = datetime.now(IST)
        req_timestamp = req_time.strftime("%Y-%m-%dT%H:%M:%S.%fZ")

        data = str(request.data)
        form = request.form
        json_v = request.get_json(silent=True)
        ip_address = request.headers['X-Real-IP']

        postData.insert_one({"method": "POST",
                             "device_ip": ip_address,
                             "req_data": data,
                             "req_form": form,
                             "req_json": json_v,
                             "request_time": req_timestamp})
        return ""


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=False, host="0.0.0.0", port=1145)
