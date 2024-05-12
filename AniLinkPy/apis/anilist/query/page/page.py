"""
This module contains the Page class which represents a Page in the AniLink API.
"""


class Page:
    """
    This class represents a Page in the AniLink API.
    """

    def users(self, variables: dict) -> dict:
        """
        This method is used to get users.

        Args:
            variables (dict): The variables for the Query.

        Returns:
            dict: The response from the users Query.
        """
