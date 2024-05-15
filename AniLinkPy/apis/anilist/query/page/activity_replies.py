from typing import Dict, Union

from AniLinkPy.apis.anilist.schemas.activity_schema import ACTIVITYREPLYSCHEMA
from AniLinkPy.base.RequestHandler import send_request


class ActivityRepliesQuery:
    """
    This class represents an Activity_Replies_schema Query in the AniLink API.

    Attributes:
        base_url (str): The base URL for the AniLink API.
        auth_token (str): The authentication token.
    """

    def __init__(self, auth_token: Union[str, None]) -> None:
        """
        The constructor for the ActivityRepliesQuery class.

        Args:
            auth_token (str): The authentication token.
        """
        self.base_url = "https://graphql.anilist.co"
        self.auth_token = auth_token

    def activityReplies(
        self, variables: Union[Dict[str, Union[str, int, bool]]]
    ) -> dict:
        """
        This method is used to send an ActivityReplies Query.

        Args:
            variables (dict): The variables for the Query.

        Raises:
            ValueError: If no variables are provided.

        Returns:
            dict: The response from the ActivityReplies Query.
        """

        query = f"""
            query ($page: Int, $perPage: Int, $id: Int, $activityId: Int, $asHtml: Boolean) {{
                Page (page: $page, perPage: $perPage) {{
                  pageInfo {{
                    total
                    perPage
                    currentPage
                    lastPage
                    hasNextPage
                  }}
                  activityReplies (id: $id, activityId: $activityId) {{
                    {ACTIVITYREPLYSCHEMA}
                  }}
                }}
              }}
        """

        data = {"query": query, "variables": variables}
        return send_request(self.base_url, "POST", data, self.auth_token)
