import json
import os
from os import listdir
import subprocess
from error import ErrorMessage
from flask import Flask, jsonify, send_file

app = Flask(__name__)


@app.route('/api/video/download/<video_id>', methods=['GET'])
def download_video(video_id):
    # call youtube-dl to download the video
    proc = subprocess.Popen(["youtube-dl", video_id, '--write-thumbnail', '--write-info-json', '-f', 'worst'])
    # wait for the process to finish
    proc.wait()
    proc.communicate()
    # check the call succeeded
    if proc.returncode != 0:
        # if the return code is not 0, return 404 error
        return json.dumps(
            ErrorMessage(404, "Error downloading video with id=" + video_id, video_id).toJson()
        ), 404
    # if the return code is 0, check if the video file exists
    json_file_array = [f for f in listdir() if video_id + ".info.json" in f]
    if not json_file_array:
        # if the video file does not exist, return 404 error
        return json.dumps(
            ErrorMessage(404, "Video information in JSON file with id=" + video_id + " not found.", video_id).toJson()
        ), 404
    else:
        # if the video file exists, read the JSON file and return the video info as JSON
        json_file = json_file_array[0]
        with open(json_file) as json_data:
            pretty_json = json.load(json_data)
        return jsonify(status="True", result=pretty_json), 200


@app.route('/api/video/thumbnail/<video_id>', methods=['GET'])
def get_thumbnail(video_id):
    # try to find the thumbnail file
    image_name = video_id + ".webp"
    image_file_array = [f for f in listdir() if image_name in f]
    if not image_file_array:
        # if the thumbnail file does not exist, raise an exception
        return json.dumps(
            ErrorMessage(404, "Video thumbnail with id=" + video_id + " not found.", video_id).toJson()
        ), 404
    else:
        # if the thumbnail file exists, return the thumbnail file
        image_file = image_file_array[0]
        return send_file(image_file)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
