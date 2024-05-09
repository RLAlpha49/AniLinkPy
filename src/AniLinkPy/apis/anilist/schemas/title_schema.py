"""
This is the TitleSchema for the Anilist API. It defines the structure of the title data that is expected to be returned from the API.

Attributes:
    romaji (str): The title in romaji.
    english (str): The title in English.
    native (str): The title in the native language.
    userPreferred (str): The user's preferred title.
"""
TitleSchema = """
title {
  romaji
  english
  native
  userPreferred
}
"""
