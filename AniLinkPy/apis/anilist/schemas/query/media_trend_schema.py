from AniLinkPy.apis.anilist.schemas.query.media_schema import MEDIASCHEMA

MEDIATRENDSCHEMA = f"""
  mediaId
  date
  trending
  averageScore
  popularity
  inProgress
  releasing
  episode
  media {{
    {MEDIASCHEMA}
  }}
"""

"""
MediaTrendSchema is a string representing the GraphQL schema for a media trend query. It includes the media's id,
date, trending status, average score, popularity, in progress status, releasing status, episode number, and media of
type `Media`.

Attributes:
    mediaId (int): The id of the media.
    date (int): The date of the media trend.
    trending (int): The trending status of the media.
    averageScore (int): The average score of the media.
    popularity (int): The popularity of the media.
    inProgress (bool): The in progress status of the media.
    releasing (bool): The releasing status of the media.
    episode (int): The episode number of the media.
    media (str): The media schema of the media.
"""
