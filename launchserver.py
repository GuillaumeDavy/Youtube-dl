import os
import subprocess

currentDirectory = os.getcwd()
os.chdir(currentDirectory + '/api')
subprocess.call(" python main.py", shell=True)