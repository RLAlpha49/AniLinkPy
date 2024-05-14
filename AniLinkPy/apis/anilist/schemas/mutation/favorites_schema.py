from AniLinkPy.apis.anilist.schemas.title_schema import TITLESCHEMA

FAVORITESSCHEMA = f"""
  anime {{
    edges {{
      id
      node {{
        id
        {TITLESCHEMA}
      }}
    }}
    nodes {{
      id
      {TITLESCHEMA}
    }}
  }}
  manga {{
    edges {{
      id
      node {{
        id
        {TITLESCHEMA}
      }}
    }}
    nodes {{
      id
      {TITLESCHEMA}
    }}
  }}
  characters {{
    edges {{
      id
      node {{
        id
        name {{
          full
        }}
      }}
    }}
    nodes {{
      id
      name {{
        full
      }}
    }}
  }}
  staff {{
    edges {{
      id
      node {{
        id
        name {{
          full
        }}
      }}
    }}
    nodes {{
      id
      name {{
        full
      }}
    }}
  }}
  studios {{
    edges {{
      id
      node {{
        id
        name
      }}
    }}
    nodes {{
      id
      name
    }}
  }}
"""

"""
FavouritesSchema is a string representing the GraphQL schema for a favourites query.
It includes the anime, manga, characters, staff, and studios schema.

Attributes:
    anime (str): The anime schema of the favourites.
    manga (str): The manga schema of the favourites.
    characters (str): The characters schema of the favourites.
    staff (str): The staff schema of the favourites.
    studios (str): The studios schema of the favourites.
"""
