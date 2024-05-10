"""
This module contains the AniList class which represents the AniList API.
"""

from AniLinkPy.apis.anilist.mutation.mutation import Mutation
from AniLinkPy.apis.anilist.query.query import Query


# pylint: disable=too-few-public-methods
class AniList:
    """
    This class represents the AniList API.

    Attributes:
        query (Query): An instance of the Query class.
        mutation (Mutation): An instance of the Mutation class.
    """

    def __init__(self, auth_token):
        """
        The constructor for AniList class.

        Args:
            auth_token (str): The authentication token.
        """
        self.query = Query(auth_token)
        self.mutation = Mutation()
