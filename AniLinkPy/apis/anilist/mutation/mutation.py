"""
This module contains the Mutation class which represents a mutation in the AniLink API.
"""


class Mutation:
    """
    This class represents a Mutation in the AniLink API.
    """

    def updateuser(self, variables: dict) -> dict:
        """
        This method is used to update a user.

        Args:
            variables (dict): The variables for the mutation.

        Returns:
            dict: The response from the updateuser Mutation.
        """
