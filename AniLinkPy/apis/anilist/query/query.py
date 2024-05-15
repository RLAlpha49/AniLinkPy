from typing import Dict, Union

from AniLinkPy.apis.anilist.query.media import MediaQuery
from AniLinkPy.apis.anilist.query.page.page import Page
from AniLinkPy.apis.anilist.query.user import UserQuery


class Query:
    """
    This class represents a Query in the AniLink API.

    Attributes:
        page (Page): An instance of the Page class.
        user_query (UserQuery): An instance of the UserQuery class.
    """

    def __init__(self, auth_token: Union[str, None]) -> None:
        """
        The constructor for Query class.

        Args:
            auth_token (str): The authentication token.
        """
        self.page = Page(auth_token)
        self.user_query = UserQuery(auth_token)
        self.media_query = MediaQuery(auth_token)

    def user(self, variables: Union[Dict[str, Union[str, int, bool]]]) -> dict:
        """
        This method is used to get a user.

        Args:
            variables (dict): The variables for the Query.

        Returns:
            dict: The response from the user Query.
        """
        return self.user_query.user(variables)

    def media(self, variables: Union[Dict[str, Union[str, int, bool]]]) -> dict:
        """
        This method is used to get a media.

        Args:
            variables (dict): The variables for the Query.

        Returns:
            dict: The response from the media Query.
        """
        return self.media_query.media(variables)
