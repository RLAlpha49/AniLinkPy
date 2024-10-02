from typing import List, Union


class RequestError(Exception):
    """Raised when there is an error in the request response."""

    def __init__(self, errors: Union[str, List[str]]) -> None:
        """
        Initialize a RequestError instance.
        
        Args:
            errors (Union[str, List[str]]): A string or list of strings representing the error(s) encountered during the request.
        
        Returns:
            None: This method doesn't return anything, it initializes the object.
        """
        self.errors = errors
        super().__init__(f"Request Error: {self.errors}")


class UnsupportedMethodError(Exception):
    """Raised when an unsupported method is provided to the send_request function."""

    def __init__(self, method: str) -> None:
        """Initialize an UnsupportedMethodError exception.
        
        Args:
            method (str): The unsupported HTTP method.
        
        Returns:
            None: This method doesn't return anything.
        """
        self.method = method
        super().__init__(f"Unsupported method: {self.method}")
