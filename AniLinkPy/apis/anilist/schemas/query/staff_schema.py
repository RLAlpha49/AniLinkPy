from AniLinkPy.apis.anilist.schemas.fuzzy_date_schema import FUZZYDATESCHEMA
from AniLinkPy.apis.anilist.schemas.image_schema import IMAGESCHEMA
from AniLinkPy.apis.anilist.schemas.name_schema import NAMESCHEMA
from AniLinkPy.apis.anilist.schemas.title_schema import TITLESCHEMA

STAFFSCHEMA = f"""
  id
  {NAMESCHEMA}
  languageV2
  {IMAGESCHEMA}
  description(asHtml: $asHtml)
  primaryOccupations
  gender
  dateOfBirth {{
    {FUZZYDATESCHEMA}
  }}
  dateOfDeath {{
    {FUZZYDATESCHEMA} }} age yearsActive homeTown bloodType isFavourite isFavouriteBlocked siteUrl staffMedia (sort:
    $staffMediaSort, type: $staffMediaType, onList: $staffMediaOnList, page: $staffMediaPage,
    perPage: $staffMediaPerPage) {{ nodes {{ id {TITLESCHEMA}
    }}
  }}
  characters (sort: $charactersSort, page: $charactersPage, perPage: $charactersPerPage) {{
    nodes {{
      id
      {NAMESCHEMA} }} }} characterMedia (sort: $characterMediaSort, onList: $characterMediaOnList,
      page: $characterMediaPage, perPage: $characterMediaPerPage) {{ nodes {{ id {TITLESCHEMA}
    }}
  }}
  submitter {{
    id
    name
  }}
  submissionStatus
  submissionNotes
  favourites
  modNotes
"""

"""
StaffSchema is a string representing the GraphQL schema for a staff query. It includes the staff's id, name,
language, image, description, primary occupations, gender, date of birth, date of death, age, years active, hometown,
blood type, favourite status, favourite blocked status, site url, staff media, characters, character media, staff,
submitter, submission status, submission notes, favourites, and mod notes.

Attributes:
    id (int): The id of the staff.
    name (str): The name schema of the staff.
    languageV2 (str): The language of the staff.
    image (str): The image schema of the staff.
    description (str): The description of the staff.
    primaryOccupations (list): The primary occupations of the staff.
    gender (str): The gender of the staff.
    dateOfBirth (str): The fuzzy date schema of the staff's date of birth.
    dateOfDeath (str): The fuzzy date schema of the staff's date of death.
    age (int): The age of the staff.
    yearsActive (int): The years active of the staff.
    homeTown (str): The hometown of the staff.
    bloodType (str): The blood type of the staff.
    isFavourite (bool): The favourite status of the staff.
    isFavouriteBlocked (bool): The favourite blocked status of the staff.
    siteUrl (str): The site url of the staff.
    staffMedia (str): The staff media schema of the staff.
    characters (str): The characters schema of the staff.
    characterMedia (str): The character media schema of the staff.
    submitter (str): The submitter of the staff.
    submissionStatus (int): The submission status of the staff.
    submissionNotes (str): The submission notes of the staff.
    favourites (int): The favourites of the staff.
    modNotes (str): The mod notes of the staff.
"""
