from typing import Union

from AniLinkPy.apis.anilist.custom import CustomRequest
from AniLinkPy.apis.anilist.mutation.mutation import Mutation
from AniLinkPy.apis.anilist.query.query import Query


# pylint: disable=too-few-public-methods
class AniList:
    """
    This class represents the AniList API.

    Attributes:
        query (Query): An instance of the Query class.
        mutation (Mutation): An instance of the Mutation class.
        custom_query (CustomRequest): An instance of the CustomRequest class.
    """

    def __init__(self, auth_token: Union[str, None]) -> None:
        """
        The constructor for AniList class.

        Args:
            auth_token (str): The authentication token.
        """
        self.query = Query(auth_token)
        self.mutation = Mutation()
        self.custom_query = CustomRequest(auth_token)

    def custom(self, query: str, variables: dict) -> dict:
        """
        This method is used to send a custom Query or Mutation.

        Args:
            query (str): The Query string.
            variables (dict): The variables for the Query.

        Returns:
            dict: The response from the custom Query.
        """
        return self.custom_query.custom(query, variables)
