import json
import os
import sys
from os import listdir

from flask import Flask, jsonify

import youtube_dl

app = Flask(__name__)


@app.route('/api/video/<video_url>', methods=['GET'])
def get_video(video_url):
    sys.argv.append('--write-thumbnail')
    sys.argv.append('--write-info-json')
    sys.argv.append(video_url)
    youtube_dl.main()
    json_file = [f for f in listdir() if ".json" in f][0]
    with open(json_file) as json_data:
        pretty_json = json.load(json_data)
        os.remove(json_file)
    return jsonify(status="True", result=pretty_json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)