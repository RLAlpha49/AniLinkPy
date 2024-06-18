from typing import Dict, Union, List

from AniLinkPy.apis.anilist.schemas.query.user_schema import USERSCHEMA
from AniLinkPy.base.RequestHandler import send_request


class FollowersQuery:
    """
    This class represents a Followers_schema Query in the AniLink API.

    Attributes:
        base_url (str): The base URL for the AniLink API.
        auth_token (str): The authentication token.
    """

    def __init__(self, auth_token: Union[str, None]) -> None:
        """
        The constructor for the FollowersQuery class.

        Args:
            auth_token (str): The authentication token.
        """
        self.base_url = "https://graphql.anilist.co"
        self.auth_token = auth_token

    def followers(
        self, variables: Union[Dict[str, Union[str, int, bool, List[str]]]]
    ) -> dict:
        """
        This method is used to send an followers Query.

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
        lastPage hasNextPage }} followers (userId: $userId, sort: $sort) {{ {USERSCHEMA} }}}}}}
        """

        data = {"query": query, "variables": variables}
        return send_request(self.base_url, "POST", data, self.auth_token)
