"""
This module contains the AniLink class which represents the AniLink API.
"""

# pylint: disable=invalid-name
from AniLinkPy.apis.anilist.anilist import AniList


# pylint: disable=too-few-public-methods
class AniLink:
    """
    This class represents the AniLink API.

    Attributes:
        auth_token (str): The authentication token.
        anilist (AniList): An instance of the AniList class.
    """

    def __init__(self, auth_token=None):
        """
        The constructor for AniLink class.

        Args:
            auth_token (str, optional): The authentication token. Defaults to None.
        """
        self.auth_token = auth_token
        self.anilist = AniList(self.auth_token)
