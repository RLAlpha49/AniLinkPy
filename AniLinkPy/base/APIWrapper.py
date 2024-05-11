# pylint: disable=invalid-name
class APIWrapper:
    """
    This class represents a wrapper for the API.

    Attributes:
        base_url (str): The base URL for the API.
    """

    def __init__(self, base_url):
        """
        The constructor for the APIWrapper class.

        Args:
            base_url (str): The base URL for the API.
        """
        self.base_url = base_url
