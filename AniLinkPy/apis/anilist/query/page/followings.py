from typing import Dict, Union

from AniLinkPy.apis.anilist.schemas.query.user_schema import USERSCHEMA
from AniLinkPy.base.RequestHandler import send_request


class FollowingsQuery:
    """
    This class represents a Followings_schema Query in the AniLink API.

    Attributes:
        base_url (str): The base URL for the AniLink API.
        auth_token (str): The authentication token.
    """

    def __init__(self, auth_token: Union[str, None]) -> None:
        """
        The constructor for the FollowingsQuery class.

        Args:
            auth_token (str): The authentication token.
        """
        self.base_url = "https://graphql.anilist.co"
        self.auth_token = auth_token

    def followings(self, variables: Union[Dict[str, Union[str, int, bool]]]) -> dict:
        """
        This method is used to send a followings Query.

        Args:
            variables (dict): The variables for the Query.

        Raises:
            ValueError: If no variables are provided.

        Returns:
            dict: The response from the airingSchedules Query.
        """

        query = f"""
        query ($page: Int, $perPage: Int, $userId: Int!, $sort: [UserSort], $asHtml: Boolean,
        $animeStatLimit: Int, $mangaStatLimit: Int, $animeStatSort: [UserStatisticsSort], $mangaStatSort: [
        UserStatisticsSort]) {{ Page (page: $page, perPage: $perPage) {{ pageInfo {{ total perPage currentPage
        lastPage hasNextPage }} following (userId: $userId, sort: $sort) {{ {USERSCHEMA} }}}}}}
        """

        data = {"query": query, "variables": variables}
        return send_request(self.base_url, "POST", data, self.auth_token)
