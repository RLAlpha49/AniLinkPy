from src.AniLinkPy.apis.anilist.query.User import UserQuery


class Page:
    def users(self, user_ids):
        pass  # Implement the method


class Query:
    def __init__(self, auth_token):
        self.page = Page()
        self.user_query = UserQuery(auth_token)

    def user(self, variables):
        return self.user_query.user(variables)


class Mutation:
    def updateuser(self, variables):
        pass  # Implement the method


class AniList:
    def __init__(self, auth_token):
        self.query = Query(auth_token)
        self.mutation = Mutation()


class AniLink:
    def __init__(self, auth_token):
        self.auth_token = auth_token
        self.anilist = AniList(self.auth_token)

    def user(self, variables):
        return self.anilist.query.user(variables)
