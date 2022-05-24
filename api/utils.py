import subprocess
import shutil
from os import listdir
from error import YoutubeVideoNotFound, FileNotFound

info_directory = "../videos/info"
video_directory = "../videos/video"
thumbnail_directory = "../videos/thumbnail"


def is_video_already_downloaded(video_id):
    """
    Check if the video has already been downloaded.
    """
    json_file_array = [f for f in listdir(info_directory) if video_id + ".info.json" in f]
    video_file_array = [f for f in listdir(video_directory) if video_id + ".mp4" in f]
    thumbnail_file_array = [f for f in listdir(thumbnail_directory) if video_id + ".webp" in f]

    if json_file_array and video_file_array and thumbnail_file_array:
        return True
    return False


def execute_download(video_id):
    """
    Execute the download of the video then check the return code
    to see if the download was successful.
    If not, raise an exception.
    """
    # call youtube-dl to download the video
    proc = subprocess.Popen(["youtube-dl", video_id, '--write-thumbnail', '--write-info-json', '-f', 'worst'])
    # wait for the process to finish
    proc.wait()
    proc.communicate()
    # check the call succeeded
    if proc.returncode != 0:
        # if the return code is not 0, raise an exception
        raise YoutubeVideoNotFound("Video with id=" + video_id + " not found on Youtube.")


def check_files_exist(json_file_array, video_file_array, thumbnail_file_array):
    """
    Check if the video info file, video file, and thumbnail file exist,
    if not, raise an exception.
    """
    check_file_exists(json_file_array, "Video information in JSON file with id=" + video_id + " not found.")
    check_file_exists(video_file_array, "Video file with id=" + video_id + " not found.")
    check_file_exists(thumbnail_file_array, "Video thumbnail file with id=" + video_id + " not found.")


def check_file_exists(file_array, error_message):
    """
    Check if the file exists, if not, raise an exception.
    """
    if not file_array:
        # if the file does not exist, raise an exception
        raise FileNotFound(error_message)


def move_files(json_file_array, video_file_array, thumbnail_file_array):
    """
    Move the video info file, video file, and thumbnail file to the videos directory.
    """
    shutil.move(json_file_array[0], info_directory)
    shutil.move(thumbnail_file_array[0], thumbnail_directory)
    shutil.move(video_file_array[0], video_directory)
