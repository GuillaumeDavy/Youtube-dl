class ErrorMessage:
    """
    Error class that is return when a problem occurs
    """

    def __init__(self, code, error, video_id):
        self.code = code
        self.error = error
        self.video_id = video_id

    def __str__(self):
        return "Error " + self.code + " for video ID " + self.video_id + " : " + self.message

    def toJson(self):
        return {
            "code": self.code,
            "video_id": self.video_id,
            "error": self.error.get_message()
        }


class YoutubeVideoNotFound(Exception):
    """
    Exception class that is raised when a video is not found on youtube
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message

    def get_message(self):
        return self.message


class FileNotFound(Exception):
    """
    Exception class that is raised when a file is not found
    """

    def __init__(self, message):
        super().__init__(message)
        self.message = message

    def __str__(self):
        return self.message

    def get_message(self):
        return self.message
