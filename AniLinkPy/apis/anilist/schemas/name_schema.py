"""
This is the NameSchema for the Anilist API. It defines the structure of the name data that is expected to be
returned from the API.

Attributes:
    first (str): The user's first name.
    last (str): The user's last name.
    full (str): The user's full name.
    native (str): The user's name in their native language.
"""

NAMESCHEMA = """
name {
first
last
full
native
}
"""
