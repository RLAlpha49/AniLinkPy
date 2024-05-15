from typing import Dict, Union

from AniLinkPy.apis.anilist.schemas.activity_schema import ACTIVITYWITHREPLIESSCHEMA
from AniLinkPy.base.RequestHandler import send_request


class ActivitiesQuery:
    """
    This class represents an Activities_schema Query in the AniLink API.

    Attributes:
        base_url (str): The base URL for the AniLink API.
        auth_token (str): The authentication token.
    """

    def __init__(self, auth_token: Union[str, None]) -> None:
        """
        The constructor for the ActivitiesQuery class.

        Args:
            auth_token (str): The authentication token.
        """
        self.base_url = "https://graphql.anilist.co"
        self.auth_token = auth_token

    def activities(self, variables: Union[Dict[str, Union[str, int, bool]]]) -> dict:
        """
        This method is used to send an activities Query.

        Args:
            variables (dict): The variables for the Query.

        Raises:
            ValueError: If no variables are provided.

        Returns:
            dict: The response from the activities Query.
        """

        query = f"""
        query ($page: Int, $perPage: Int, $id: Int, $userId: Int, $messengerId: Int, $mediaId: Int,
        $type: ActivityType, $isFollowing: Boolean, $hasReplies: Boolean, $hasRepliesOrTypeText: Boolean, $createdAt:
        Int, $id_not: Int, $id_in: [Int], $id_not_in: [Int], $userId_not: Int, $userId_in: [Int], $userId_not_in: [
        Int], $messengerId_not: Int, $messengerId_in: [Int], $messengerId_not_in: [Int], $mediaId_not: Int,
        $mediaId_in: [Int], $mediaId_not_in: [Int], $type_not: ActivityType, $type_in: [ActivityType], $type_not_in:
        [ActivityType], $createdAt_greater: Int, $sort: [ActivitySort], $asHtml: Boolean) {{ Page (page: $page,
        perPage: $perPage) {{ pageInfo {{ total perPage currentPage lastPage hasNextPage }} activities (id: $id,
        userId: $userId, messengerId: $messengerId, mediaId: $mediaId, type: $type, isFollowing: $isFollowing,
        hasReplies: $hasReplies, hasRepliesOrTypeText: $hasRepliesOrTypeText, createdAt: $createdAt, id_not: $id_not,
        id_in: $id_in, id_not_in: $id_not_in, userId_not: $userId_not, userId_in: $userId_in, userId_not_in:
        $userId_not_in, messengerId_not: $messengerId_not, messengerId_in: $messengerId_in, messengerId_not_in:
        $messengerId_not_in, mediaId_not: $mediaId_not, mediaId_in: $mediaId_in, mediaId_not_in: $mediaId_not_in,
        type_not: $type_not, type_in: $type_in, type_not_in: $type_not_in, createdAt_greater: $createdAt_greater,
        sort: $sort) {{ {ACTIVITYWITHREPLIESSCHEMA} }}}}}}
        """

        data = {"query": query, "variables": variables}
        return send_request(self.base_url, "POST", data, self.auth_token)
