from src.AniLinkPy.apis.anilist.schemas.query.user_schema import UserSchema
from src.AniLinkPy.base.RequestHandler import send_request


class UserQuery:
    def __init__(self, auth_token):
        self.base_url = 'https://graphql.anilist.co'
        self.auth_token = auth_token

    def user(self, variables):
        if not variables:
            raise ValueError('At least one variable must be provided')

        query = f"""
            query ($id: Int, $name: String, $isModerator: Boolean, $search: String, $sort: [UserSort], $asHtml: Boolean, $animeStatLimit: Int, $mangaStatLimit: Int, $animeStatSort: [UserStatisticsSort], $mangaStatSort: [UserStatisticsSort]) {{
                User (id: $id, name: $name, isModerator: $isModerator, search: $search, sort: $sort) {{
                    {UserSchema}
                }}
            }}
        """

        data = {'query': query, 'variables': variables}
        return send_request(self.base_url, 'POST', data, self.auth_token)
