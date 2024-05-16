from typing import Dict, Union

from AniLinkPy.apis.anilist.schemas.query.character_schema import CHARACTERSCHEMA
from AniLinkPy.base.RequestHandler import send_request


class CharactersQuery:
    """
    This class represents a Characters_schema Query in the AniLink API.

    Attributes:
        base_url (str): The base URL for the AniLink API.
        auth_token (str): The authentication token.
    """

    def __init__(self, auth_token: Union[str, None]) -> None:
        """
        The constructor for the CharactersQuery class.

        Args:
            auth_token (str): The authentication token.
        """
        self.base_url = "https://graphql.anilist.co"
        self.auth_token = auth_token

    def characters(self, variables: Union[Dict[str, Union[str, int, bool]]]) -> dict:
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
        query ($page: Int, $perPage: Int, $id: Int, $isBirthday: Boolean, $search: String, $id_not: Int,
        $id_in: [Int], $id_not_in: [Int], $sort: [CharacterSort], $asHtml: Boolean, $mediaSort: [MediaSort],
        $mediaOnList: Boolean, $mediaPage: Int, $mediaPerPage: Int) {{ Page (page: $page, perPage: $perPage) {{
        pageInfo {{ total perPage currentPage lastPage hasNextPage }} characters (id: $id, isBirthday: $isBirthday,
        search: $search, id_not: $id_not, id_in: $id_in, id_not_in: $id_not_in, sort: $sort) {{ {CHARACTERSCHEMA} }}}}}}
        """

        data = {"query": query, "variables": variables}
        return send_request(self.base_url, "POST", data, self.auth_token)
