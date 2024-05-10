from src.AniLinkPy.base.RequestHandler import send_request


class CustomRequest:
    """
    This class represents a custom request in the AniLink API.

    Attributes:
        base_url (str): The base URL for the AniLink API.
        auth_token (str): The authentication token.
    """

    def __init__(self, auth_token):
        """
        The constructor for the CustomRequest class.

        Args:
            auth_token (str): The authentication token.
        """
        self.base_url = "https://graphql.anilist.co"
        self.auth_token = auth_token

    def custom(self, query, variables=None):
        """
        This method is used to send a custom query.

        Args:
            query (str): The query string.
            variables (dict, optional): The variables for the query. Defaults to None.

        Returns:
            dict: The response from the custom query.
        """
        if variables is None:
            variables = {}

        data = {"query": query, "variables": variables}
        return send_request(self.base_url, "POST", data, self.auth_token)
