"""
This is the TagSchema for the Anilist API. It defines the structure of the tag data that is expected to be
returned from the API.

Attributes:
    id (int): The tag's ID.
    name (str): The tag's name.
    description (str): The tag's description.
    category (str): The tag's category.
    rank (int): The tag's rank.
    isGeneralSpoiler (bool): Whether the tag is a general spoiler.
    isMediaSpoiler (bool): Whether the tag is a media spoiler.
    isAdult (bool): Whether the tag is adult.
    userId (int): The user's ID.
"""

TAGSCHEMA = """
id
name
description
category
rank
isGeneralSpoiler
isMediaSpoiler
isAdult
userId
"""
