class RequestError(Exception):
    """Raised when there is an error in the request response."""

    def __init__(self, errors):
        self.errors = errors
        super().__init__(f"Request Error: {self.errors}")


class UnsupportedMethodError(Exception):
    """Raised when an unsupported method is provided to the send_request function."""

    def __init__(self, method):
        self.method = method
        super().__init__(f"Unsupported method: {self.method}")
