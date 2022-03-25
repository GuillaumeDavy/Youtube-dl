import os
import subprocess

subprocess.call("docker build -t youtube-dl-docker .", shell=True)
subprocess.call("docker run --name youtube-dl-docker -p 5001:5001 youtube-dl-docker", shell=True)
