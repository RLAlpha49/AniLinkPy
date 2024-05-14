from AniLinkPy.apis.anilist.schemas.fuzzy_date_schema import FUZZYDATESCHEMA
from AniLinkPy.apis.anilist.schemas.image_schema import IMAGESCHEMA
from AniLinkPy.apis.anilist.schemas.name_schema import NAMESCHEMA
from AniLinkPy.apis.anilist.schemas.title_schema import TITLESCHEMA

CHARACTERSCHEMA = f"""
  id
  {NAMESCHEMA}
  {IMAGESCHEMA}
  description(asHtml: $asHtml)
  gender
  dateOfBirth {{
    {FUZZYDATESCHEMA}
  }}
  age
  bloodType
  isFavourite
  isFavouriteBlocked
  siteUrl
  media(sort: $mediaSort, onList: $mediaOnList, page: $mediaPage, perPage: $mediaPerPage) {{
    nodes {{
      id
      {TITLESCHEMA}
    }}
  }}
  favourites
  modNotes
"""

"""
CharacterSchema is a string representing the GraphQL schema for a character query. It includes the character's id,
name, image, description, gender, date of birth, age, blood type, favourite status, site URL, associated media,
number of favourites, and moderator notes.

Attributes:
    id (int): The id of the character.
    name (str): The name schema of the character.
    image (str): The image schema of the character.
    description (str): The description of the character.
    gender (str): The gender of the character.
    dateOfBirth (str): The fuzzy date schema of the character's date of birth.
    age (int): The age of the character.
    bloodType (str): The blood type of the character.
    isFavourite (bool): The favourite status of the character.
    isFavouriteBlocked (bool): The favourite blocked status of the character.
    siteUrl (str): The site URL of the character.
    media (str): The media schema of the character.
    favourites (int): The number of favourites of the character.
    modNotes (str): The moderator notes of the character.
"""
