"""
This is the CoverImageSchema for the Anilist API. It defines the structure of the cover image data that is
expected to be returned from the API.

Attributes:
    extraLarge (str): The URL of the extra large cover image.
    large (str): The URL of the large cover image.
    medium (str): The URL of the medium cover image.
"""

COVERIMAGESCHEMA = """
coverImage {
  extraLarge
  large
  medium
}
"""
