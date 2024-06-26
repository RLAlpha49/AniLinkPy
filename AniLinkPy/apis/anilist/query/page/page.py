"""
This module contains the Page class which represents a Page in the AniLink API.
"""

from typing import Dict, Union, List

from AniLinkPy.apis.anilist.query.page.activities import ActivitiesQuery
from AniLinkPy.apis.anilist.query.page.activity_replies import ActivityRepliesQuery
from AniLinkPy.apis.anilist.query.page.airing_schedules import AiringSchedulesQuery
from AniLinkPy.apis.anilist.query.page.characters import CharactersQuery
from AniLinkPy.apis.anilist.query.page.followers import FollowersQuery
from AniLinkPy.apis.anilist.query.page.followings import FollowingsQuery


class Page:
    """
    This class represents a Page in the AniLink API.
    """

    def __init__(self, auth_token: Union[str, None]) -> None:
        """
        The constructor for Page class.

        Args:
            auth_token (str): The authentication token.
        """
        self.activities_query = ActivitiesQuery(auth_token)
        self.activity_replies_query = ActivityRepliesQuery(auth_token)
        self.airing_schedules_query = AiringSchedulesQuery(auth_token)
        self.characters_query = CharactersQuery(auth_token)
        self.followers_query = FollowersQuery(auth_token)
        self.followings_query = FollowingsQuery(auth_token)

    def activities(
        self, variables: Union[Dict[str, Union[str, int, bool]], None] = None
    ) -> dict:
        """
        This method is used to get activities.

        Args:
            variables (dict): The variables for the Query.

        Returns:
            dict: The response from the activities Query.
        """
        if variables is None:
            variables = {}
        return self.activities_query.activities(variables)

    def activityReplies(
        self, variables: Union[Dict[str, Union[str, int, bool]], None] = None
    ) -> dict:
        """
        This method is used to get activity_replies.

        Args:
            variables (dict): The variables for the Query.

        Returns:
            dict: The response from the activity_replies Query.
        """
        if variables is None:
            variables = {}
        return self.activity_replies_query.activityReplies(variables)

    def airingSchedules(
        self, variables: Union[Dict[str, Union[str, int, bool]], None] = None
    ) -> dict:
        """
        This method is used to get airing_schedules.

        Args:
            variables (dict): The variables for the Query.

        Returns:
            dict: The response from the airing_schedules Query.
        """
        if variables is None:
            variables = {}
        return self.airing_schedules_query.airingSchedules(variables)

    def characters(
        self, variables: Union[Dict[str, Union[str, int, bool]], None] = None
    ) -> dict:
        """
        This method is used to get characters.

        Args:
            variables (dict): The variables for the Query.

        Returns:
            dict: The response from the characters Query.
        """
        if variables is None:
            variables = {}
        return self.characters_query.characters(variables)

    def followers(
        self, variables: Union[Dict[str, Union[str, int, bool, List[str]]], None] = None
    ) -> dict:
        """
        This method is used to get followers.

        Args:
            variables (dict): The variables for the Query.

        Returns:
            dict: The response from the followers Query.
        """
        if variables is None:
            variables = {}
        return self.followers_query.followers(variables)

    def followings(
        self, variables: Union[Dict[str, Union[str, int, bool, List[str]]], None] = None
    ) -> dict:
        """
        This method is used to get followings.

        Args:
            variables (dict): The variables for the Query.

        Returns:
            dict: The response from the followings Query.
        """
        if variables is None:
            variables = {}
        return self.followings_query.followings(variables)
