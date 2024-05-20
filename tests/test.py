# pylint: disable=unnecessary-lambda
import os
import time
import unittest

from dotenv import load_dotenv

from AniLinkPy import AniLink


def handle_rate_limit(api_call, retry_after=60):
    """
    This function handles the rate limit of the API.
    :param api_call:
    :param retry_after:
    :return response:
    """
    while True:
        try:
            response = api_call()
            print(response)
            return response
        except Exception as error:  # pylint: disable=broad-except
            if "429" in str(error):
                print("Rate limit exceeded, waiting for 1 minute before retrying...")
                time.sleep(retry_after)
                print("Retrying...")
            else:
                raise error


class TestQueries(unittest.TestCase):
    """
    This class contains tests for the queries in the AniList API.
    """

    def setUp(self):
        """
        This method sets up the tests environment.
        """
        load_dotenv()
        self.auth_token = os.getenv("ANILIST_TOKEN")
        self.anilink = AniLink.AniLink(self.auth_token)

    def test_custom(self):
        """
        This method tests the custom query.
        """
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
        self.assertIsNotNone(response)

    def test_user(self):
        """
        This method tests the user query.
        """
        variables = {"id": 1}
        response = handle_rate_limit(lambda: self.anilink.anilist.query.user(variables))
        self.assertIsNotNone(response)

    def test_media(self):
        """
        This method tests the media query.
        """
        variables = {"id": 1}
        response = handle_rate_limit(
            lambda: self.anilink.anilist.query.media(variables)
        )
        self.assertIsNotNone(response)


class TestPageQueries(unittest.TestCase):
    """
    This class contains tests for the page queries in the AniList API.
    """

    def setUp(self):
        """
        This method sets up the tests environment.
        """
        load_dotenv()
        self.auth_token = os.getenv("ANILIST_TOKEN")
        self.anilink = AniLink.AniLink(self.auth_token)

    def test_activities(self):
        """
        This method tests the activities query.
        """
        response = handle_rate_limit(
            lambda: self.anilink.anilist.query.page.activities()
        )
        self.assertIsNotNone(response)

    def test_activity_replies(self):
        """
        This method tests the activity_replies query.
        """
        response = handle_rate_limit(
            lambda: self.anilink.anilist.query.page.activityReplies()
        )
        self.assertIsNotNone(response)

    def test_airing_schedules(self):
        """
        This method tests the airing_schedules query.
        """
        response = handle_rate_limit(
            lambda: self.anilink.anilist.query.page.airingSchedules()
        )
        self.assertIsNotNone(response)

    def test_characters(self):
        """
        This method tests the characters query.
        """
        response = handle_rate_limit(
            lambda: self.anilink.anilist.query.page.characters()
        )
        self.assertIsNotNone(response)

    def test_followers(self):
        """
        This method tests the followers query.
        """
        variables = {"page": 1, "perPage": 10, "userId": 1, "sort": ["ID_DESC"]}
        response = handle_rate_limit(
            lambda: self.anilink.anilist.query.page.followers(variables)
        )
        self.assertIsNotNone(response)


if __name__ == "__main__":
    unittest.main()
