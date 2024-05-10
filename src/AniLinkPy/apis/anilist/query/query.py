from src.AniLinkPy.apis.anilist.custom import CustomRequest
from src.AniLinkPy.apis.anilist.query.page.page import Page
from src.AniLinkPy.apis.anilist.query.user import UserQuery


class Query:
    """
    This class represents a Query in the AniLink API.

    Attributes:
        page (Page): An instance of the Page class.
        custom_query (CustomRequest): An instance of the CustomRequest class.
        user_query (UserQuery): An instance of the UserQuery class.
    """

    def __init__(self, auth_token):
        """
        The constructor for Query class.

        Args:
            auth_token (str): The authentication token.
        """
        self.page = Page()
        self.custom_query = CustomRequest(auth_token)
        self.user_query = UserQuery(auth_token)

    def custom(self, query, variables):
        """
        This method is used to send a custom query.

        Args:
            query (str): The query string.
            variables (dict): The variables for the query.

        Returns:
            dict: The response from the custom query.
        """
        return self.custom_query.custom(query, variables)

    def user(self, variables):
        """
        This method is used to get a user.

        Args:
            variables (dict): The variables for the query.

        Returns:
            dict: The response from the user query.
        """
        return self.user_query.user(variables)
