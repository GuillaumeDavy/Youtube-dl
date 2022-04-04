import json
import os
from os import listdir
import subprocess

from flask import Flask, jsonify, send_file

app = Flask(__name__)


@app.route('/api/video/download/<video_id>', methods=['GET'])
def download_video(video_id):
    subprocess.run(['youtube-dl', video_id, '--write-thumbnail', '--write-info-json'])
    json_file_array = [f for f in listdir() if ".json" in f]
    if not json_file_array:
        raise FileNotFoundError("Video information in JSON file with id=" + video_id + " not found.")
    else:
        json_file = json_file_array[0]
        with open(json_file) as json_data:
            pretty_json = json.load(json_data)
            os.remove(json_file)
        return jsonify(status="True", result=pretty_json)


@app.route('/api/video/thumbnail/<video_id>', methods=['GET'])
def get_thumbnail(video_id):
    image_name = video_id + ".webp"
    image_file_array = [f for f in listdir() if image_name in f]
    if not image_file_array:
        raise FileNotFoundError("Video thumbnail with id=" + video_id + " not found.")
    else:
        image_file = image_file_array[0]
        return send_file(image_file)


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5001, debug = True) 