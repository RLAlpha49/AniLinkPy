from AniLinkPy.apis.anilist.schemas.image_schema import IMAGESCHEMA
from AniLinkPy.apis.anilist.schemas.name_schema import NAMESCHEMA
from AniLinkPy.apis.anilist.schemas.query.character_schema import CHARACTERSCHEMA
from AniLinkPy.apis.anilist.schemas.query.media_schema import MEDIASCHEMA
from AniLinkPy.apis.anilist.schemas.query.staff_schema import STAFFSCHEMA

STUDIOSCHEMA = f"""
  id
  name
  isAnimationStudio
  media (sort: $mediaSort, isMain: $mediaIsMain onList: $mediaOnList, page: $mediaPage, perPage: $mediaPerPage) {{
    edges {{
      id
      relationType
      isMainStudio
      characters {{
        {CHARACTERSCHEMA}
      }}
      characterRole
      characterName
      roleNotes
      dubGroup
      voiceActors {{
        {STAFFSCHEMA}
      }}
      voiceActorRoles {{
        voiceActor {{
          id
          {NAMESCHEMA}
          {IMAGESCHEMA}
        }}
        roleNotes
        dubGroup
      }}
      favouriteOrder
      node {{
        {MEDIASCHEMA}
      }}
    }}
    nodes {{
      {MEDIASCHEMA}
    }}
    pageInfo {{
      total
      perPage
      currentPage
      lastPage
      hasNextPage
    }}
  }}
  siteUrl
  isFavourite
  favourites
"""

"""
StudioSchema is a string representing the GraphQL schema for a studio query.
It includes the studio's id, name, animation studio status, media, site url, favourite status, and favourites count.

Attributes:
    id (int): The id of the studio.
    name (str): The name of the studio.
    isAnimationStudio (bool): The animation studio status of the studio.
    media (str): The media schema of the studio.
    siteUrl (str): The site url of the studio.
    isFavourite (bool): The favourite status of the studio.
    favourites (int): The favourites count of the studio.
"""
