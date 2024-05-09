import os
import unittest

from AniLinkPy import AniLink
from dotenv import load_dotenv


class TestUserQuery(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.auth_token = os.getenv('ANILIST_TOKEN')
        self.anilink = AniLink.AniLink(self.auth_token)

    def test_custom(self):
        query = """
        query ($id: Int) {
            User (id: $id) {
                id
                name
            }
        }
        """
        variables = {'id': 1}
        response = self.anilink.anilist.query.custom(query, variables)
        print(response)
        self.assertIsNotNone(response)

    def test_user(self):
        variables = {'id': 1}
        response = self.anilink.anilist.query.user(variables)
        print(response)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
