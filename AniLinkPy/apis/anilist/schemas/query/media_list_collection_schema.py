from AniLinkPy.apis.anilist.schemas.query.media_list_schema import MEDIALISTSCHEMA

MEDIALISTCOLLECTIONSCHEMA = f"""
  lists {{
    entries {{
      {MEDIALISTSCHEMA}
    name
    isCustomList
    isSplitCompletedList
    status
    }}
  hasNextChunk
  }}
"""

"""
MediaListCollectionQuerySchema is a string representing the GraphQL schema for a media list collection query.
It includes the media list collection, lists, entries, user, and hasNextChunk status.

Attributes:
    lists (list): The lists of the media list collection.
    entries (list): The entries of the media list collection.
    hasNextChunk (bool): The hasNextChunk status of the media list collection.
"""
