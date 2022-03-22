import json
import os
from os import listdir
import subprocess

from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/api/video/<video_url>', methods=['GET'])
def get_video(video_url):
    print("Hello here")
    subprocess.run(['youtube-dl', video_url, '--write-thumbnail', '--write-info-json'])
    json_file = [f for f in listdir() if ".json" in f][0]
    with open(json_file) as json_data:
        pretty_json = json.load(json_data)
        os.remove(json_file)
    return jsonify(status="True", result=pretty_json)


if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 5001, debug = True) 