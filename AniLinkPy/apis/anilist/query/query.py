from AniLinkPy.apis.anilist.query.page.page import Page
from AniLinkPy.apis.anilist.query.user import UserQuery


class Query:
    """
    This class represents a Query in the AniLink API.

    Attributes:
        page (Page): An instance of the Page class.
        user_query (UserQuery): An instance of the UserQuery class.
    """

    def __init__(self, auth_token):
        """
        The constructor for Query class.

        Args:
            auth_token (str): The authentication token.
        """
        self.page = Page()
        self.user_query = UserQuery(auth_token)

    def user(self, variables) -> dict:
        """
        This method is used to get a user.

        Args:
            variables (dict): The variables for the Query.

        Returns:
            dict: The response from the user Query.
        """
        return self.user_query.user(variables)
