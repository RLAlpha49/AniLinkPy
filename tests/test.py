import os
import time
import unittest

from dotenv import load_dotenv

from AniLinkPy import AniLink


def handle_rate_limit(api_call, retry_after=60):
    while True:
        try:
            response = api_call()
            print(response)
            return response
        except Exception as error:
            if "429" in str(error):
                print("Rate limit exceeded, waiting for 1 minute before retrying...")
                time.sleep(retry_after)
                print("Retrying...")
            else:
                raise error


class TestQueries(unittest.TestCase):
    def setUp(self):
        load_dotenv()
        self.auth_token = os.getenv("ANILIST_TOKEN")
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
        variables = {"id": 1}
        response = handle_rate_limit(
            lambda: self.anilink.anilist.custom(query, variables)
        )
        print(response)
        self.assertIsNotNone(response)

    def test_user(self):
        variables = {"id": 1}
        response = handle_rate_limit(lambda: self.anilink.anilist.query.user(variables))
        print(response)
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
