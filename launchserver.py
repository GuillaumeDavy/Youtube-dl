import os
import subprocess

currentDirectory = os.getcwd()
os.chdir(currentDirectory + '/api')
subprocess.call("python3 main.py", shell=True)