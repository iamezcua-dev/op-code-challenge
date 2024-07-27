class MalformedConfigFileError(BaseException):
    """Raised when the config file is not well-formed"""

    def __init__(self):
        super().__init__(f"Malformed configuration!")
