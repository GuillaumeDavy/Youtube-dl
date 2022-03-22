# INSTALLATION

## Requirements for dev

1. This project require python interpreter. Please install it before going further. [Python installation](https://www.python.org/downloads/)

2. Install pip by following the [documentation](https://pip.pypa.io/en/stable/installation/) 

3. You need to install Flask by using the command `pip install Flask`

## Unix users
To install it right away for all UNIX users (Linux, macOS, etc.), type:

    sudo curl -L https://yt-dl.org/downloads/latest/youtube-dl -o /usr/local/bin/youtube-dl
    sudo chmod a+rx /usr/local/bin/youtube-dl

If you do not have curl, you can alternatively use a recent wget:

    sudo wget https://yt-dl.org/downloads/latest/youtube-dl -O /usr/local/bin/youtube-dl
    sudo chmod a+rx /usr/local/bin/youtube-dl


## Windows users
Windows users can [download an .exe file](https://yt-dl.org/latest/youtube-dl.exe) and place it in any location on their [PATH](https://en.wikipedia.org/wiki/PATH_%28variable%29) except for `%SYSTEMROOT%\System32` (e.g. **do not** put in `C:\Windows\System32`).

You can also use pip:

    sudo -H pip install --upgrade youtube-dl
    
This command will update youtube-dl if you have already installed it. See the [pypi page](https://pypi.python.org/pypi/youtube_dl) for more information.

## MacOS users

macOS users can install youtube-dl with [Homebrew](https://brew.sh/):

    brew install youtube-dl

Or with [MacPorts](https://www.macports.org/):

    sudo port install youtube-dl

Alternatively, refer to the [developer instructions](#developer-instructions) for how to check out and work with the git repository. For further options, including PGP signatures, see the [youtube-dl Download Page](https://ytdl-org.github.io/youtube-dl/download.html).

## Launch the project

DEV : To launch the project, just run `python launchserver.py`
USERS : To launch the project, just run `python launchdocker.py`, it will create a docker archive then start the docker, it may takes several minutes.

# HOW TO USE ?

1. [Download postman](https://www.postman.com/downloads/)
2. Create an HTTP GET request to `http://localhost:5001/api/video/<video_id>`

To test it, you can use the video id `668nUCeBHyY`

# DEVELOPMENT

Follow the [readme of the project](https://github.com/ytdl-org/youtube-dl)