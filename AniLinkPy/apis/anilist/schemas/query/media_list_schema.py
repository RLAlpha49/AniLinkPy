from AniLinkPy.apis.anilist.schemas.fuzzy_date_schema import FUZZYDATESCHEMA
from AniLinkPy.apis.anilist.schemas.query.media_schema import MEDIASCHEMA

MEDIALISTSCHEMA = f"""
  id
  userId
  mediaId
  status
  score (format: $ScoreFormat)
  progress
  progressVolumes
  repeat
  priority
  private
  notes
  hiddenFromStatusLists
  customLists (asArray: $asArray)
  advancedScores
  startedAt {{
    {FUZZYDATESCHEMA}
  }}
  completedAt {{
    {FUZZYDATESCHEMA}
  }}
  updatedAt
  createdAt
  media {{
    {MEDIASCHEMA}
  }}
"""

"""
MediaListSchema is a string representing the GraphQL schema for a media list query. It includes the id, user id,
media id, status, score, progress, progress volumes, repeat, priority, private status, notes, hidden from status
lists status, custom lists, advanced scores, started at date, completed at date, updated at timestamp, created at
timestamp, media, and user.

Attributes:
    id (int): The id of the media list.
    userId (int): The user id of the media list.
    mediaId (int): The media id of the media list.
    status (str): The status of the media list.
    score (str): The score of the media list.
    progress (int): The progress of the media list.
    progressVolumes (int): The progress volumes of the media list.
    repeat (int): The repeat of the media list.
    priority (int): The priority of the media list.
    private (bool): The private status of the media list.
    notes (str): The notes of the media list.
    hiddenFromStatusLists (bool): The hidden from status lists status of the media list.
    customLists (str): The custom lists of the media list.
    advancedScores (list): The advanced scores of the media list.
    startedAt (str): The started at date of the media list.
    completedAt (str): The completed at date of the media list.
    updatedAt (int): The updated at timestamp of the media list.
    createdAt (int): The created at timestamp of the media list.
    media (str): The media of the media list.
"""
