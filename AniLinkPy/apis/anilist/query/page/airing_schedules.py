from typing import Dict, Union

from AniLinkPy.apis.anilist.schemas.query.airing_schedule_schema import (
    AIRINGSCHEDULESCHEMA,
)
from AniLinkPy.base.RequestHandler import send_request


class AiringSchedulesQuery:
    """
    This class represents an Airing_Schedules_schema Query in the AniLink API.

    Attributes:
        base_url (str): The base URL for the AniLink API.
        auth_token (str): The authentication token.
    """

    def __init__(self, auth_token: Union[str, None]) -> None:
        """
        The constructor for the AiringSchedulesQuery class.

        Args:
            auth_token (str): The authentication token.
        """
        self.base_url = "https://graphql.anilist.co"
        self.auth_token = auth_token

    def airingSchedules(
        self, variables: Union[Dict[str, Union[str, int, bool]]]
    ) -> dict:
        """
        This method is used to send an airingSchedules Query.

        Args:
            variables (dict): The variables for the Query.

        Raises:
            ValueError: If no variables are provided.

        Returns:
            dict: The response from the airingSchedules Query.
        """

        query = f"""
        query ($page: Int, $perPage: Int, $id: Int, $mediaId: Int, $episode: Int, $airingAt: Int,
        $notYetAired: Boolean, $id_not: Int, $id_in: [Int], $id_not_in: [Int], $mediaId_not: Int, $mediaId_in: [Int],
        $mediaId_not_in: [Int], $episode_not: Int, $episode_in: [Int], $episode_not_in: [Int], $episode_greater: Int,
        $episode_lesser: Int, $airingAt_greater: Int, $airingAt_lesser: Int, $sort: [AiringSort], $asHtml: Boolean) {{
        Page (page: $page, perPage: $perPage) {{ pageInfo {{ total perPage currentPage lastPage hasNextPage }}
        airingSchedules (id: $id, mediaId: $mediaId, episode: $episode, airingAt: $airingAt, notYetAired: $notYetAired,
        id_not: $id_not, id_in: $id_in, id_not_in: $id_not_in, mediaId_not: $mediaId_not, mediaId_in: $mediaId_in,
        mediaId_not_in: $mediaId_not_in, episode_not: $episode_not, episode_in: $episode_in, episode_not_in:
        $episode_not_in, episode_greater: $episode_greater, episode_lesser: $episode_lesser, airingAt_greater:
        $airingAt_greater, airingAt_lesser: $airingAt_lesser, sort: $sort) {{ {AIRINGSCHEDULESCHEMA} }}}}}}
        """

        data = {"query": query, "variables": variables}
        return send_request(self.base_url, "POST", data, self.auth_token)
