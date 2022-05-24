class ErrorMessage:
    """
    Error class that is return when a problem occurs
    """

    def __init__(self, code, message, video_id):
        self.code = code
        self.message = message
        self.video_id = video_id

    def __str__(self):
        return "Error " + self.code + " for video ID " + self.video_id + " : " + self.message

    def toJson(self):
        return {
            "code": self.code,
            "video_id": self.video_id,
            "message": self.message
        }
