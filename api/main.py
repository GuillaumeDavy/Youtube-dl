import json
import os
from os import listdir
from error import ErrorMessage, YoutubeVideoNotFound
from flask import Flask, jsonify, send_file
from utils import (
    is_video_already_downloaded,
    execute_download,
    check_files_exist,
    check_file_exists,
    move_files,
    info_directory,
    video_directory,
    thumbnail_directory,
    get_thumbnail_file_array,
)
from pathlib import Path

app = Flask(__name__)


@app.route('/api/video/download/<video_id>', methods=['GET'])
def download_video(video_id):
    """
    Download the video from youtube and save it in the videos directory.
    """
    # check if the video has already been downloaded
    if(is_video_already_downloaded(video_id)) is True:
        # if the video has already been downloaded, return 409 conflict
        return jsonify("Video " + video_id + " already downloaded"), 409

    try:
        # execute the download of the video then check the return code
        execute_download(video_id)
    except YoutubeVideoNotFound as e:
        return ErrorMessage(404, e, video_id).toJson(), 404

    json_file_array = [f for f in listdir() if video_id + ".info.json" in f]
    video_file_array = [f for f in listdir() if video_id + ".mp4" in f]
    thumbnail_file_array = get_thumbnail_file_array(video_id)

    # check if the video info file, video file, and thumbnail file exist
    try:
        check_files_exist(json_file_array, video_file_array, thumbnail_file_array, video_id)
    except FileNotFound as e:
        delete_files(json_file_array, video_file_array, thumbnail_file_array)
        return ErrorMessage(404, e, video_id).toJson(), 404

    # if the video info file exists, read the JSON file and return the video info as JSON
    with open(json_file_array[0]) as json_data:
        pretty_json = json.load(json_data)

    # move the video file, thumbnail file, and info file to the videos directory
    move_files(json_file_array, video_file_array, thumbnail_file_array)

    # return the video info as JSON
    return jsonify(status="True", result=pretty_json), 200


@app.route('/api/video/thumbnail/<video_id>', methods=['GET'])
def get_thumbnail(video_id):
    """
    Get the thumbnail of the video.
    """

    # move current working directory to the videos thumbnail directory
    os.chdir(thumbnail_directory)

    image_name = video_id + ".webp"
    image_file_array = [f for f in listdir() if image_name in f]

    try:
        check_file_exists(image_file_array, "Video thumbnail file with id=" + video_id + " not found. Try downloading the video first.")
    except FileNotFound as e:
        return ErrorMessage(404, e, video_id).toJson(), 404

    # if the thumbnail file exists, return the thumbnail file
    image_file = image_file_array[0]
    path = os.getcwd() + "/" + image_file

    # move current working directory back to the root directory
    os.chdir("../../api")
    return send_file(path)


@app.route('/api/video/info/<video_id>', methods=['GET'])
def get_info(video_id):
    """
    Get the info of the video.
    """
    # move current working directory to the videos info directory
    os.chdir(info_directory)

    info_file_name = video_id + ".info.json"
    info_file_name_array = [f for f in listdir() if info_file_name in f]

    try:
        check_file_exists(info_file_name_array,
                          "Video info file with id=" + video_id + " not found. Try downloading the video first.")
    except FileNotFound as e:
        return ErrorMessage(404, e, video_id).toJson(), 404

    # if the thumbnail file exists, return the thumbnail file
    info_file = info_file_name_array[0]
    path = os.getcwd() + "/" + info_file

    # move current working directory back to the root directory
    os.chdir("../../api")
    return send_file(path)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
