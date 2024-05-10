from src.AniLinkPy.apis.anilist.schemas.query.user_schema import UserSchema
from src.AniLinkPy.base.RequestHandler import send_request


class UserQuery:
    """
    This class represents a user query in the AniLink API.

    Attributes:
        base_url (str): The base URL for the AniLink API.
        auth_token (str): The authentication token.
    """

    def __init__(self, auth_token):
        """
        The constructor for the UserQuery class.

        Args:
            auth_token (str): The authentication token.
        """
        self.base_url = "https://graphql.anilist.co"
        self.auth_token = auth_token

    def user(self, variables):
        """
        This method is used to send a user query.

        Args:
            variables (dict): The variables for the query.

        Raises:
            ValueError: If no variables are provided.

        Returns:
            dict: The response from the user query.
        """
        if not variables:
            raise ValueError("At least one variable must be provided")

        query = f""" 
            query ($id: Int, $name: String, $isModerator: Boolean, $search: String, $sort: [UserSort], 
                $asHtml: Boolean, $animeStatLimit: Int, $mangaStatLimit: Int, $animeStatSort: [UserStatisticsSort], 
                $mangaStatSort: [UserStatisticsSort]) {{ User (id: $id, name: $name, isModerator: $isModerator, 
                search: $search, sort: $sort) {{ {UserSchema}
                }}
            }}
        """

        data = {"query": query, "variables": variables}
        return send_request(self.base_url, "POST", data, self.auth_token)
