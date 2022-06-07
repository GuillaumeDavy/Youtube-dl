import os
import subprocess

subprocess.call("docker build -t youtube-dl-api .", shell=True)
subprocess.call("docker run --name youtube-dl-api -v ${HOME}/Desktop/videos:/video_storage -p 5001:5001 youtube-dl-api", shell=True)

