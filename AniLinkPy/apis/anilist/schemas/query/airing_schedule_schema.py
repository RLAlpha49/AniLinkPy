from AniLinkPy.apis.anilist.schemas.query.media_schema import MEDIASCHEMA

AIRINGSCHEDULESCHEMA = f"""
  id
  airingAt
  timeUntilAiring
  episode
  mediaId
  media {{
    {MEDIASCHEMA}
  }}
"""

"""
AiringScheduleSchema is a string representing the GraphQL schema for an airing schedule query.
It includes the id, airing time, time until airing, episode number, media id, and the media schema.

Attributes:
    id (int): The id of the airing schedule.
    airingAt (int): The airing time of the airing schedule.
    timeUntilAiring (int): The time until airing of the airing schedule.
    episode (int): The episode number of the airing schedule.
    mediaId (int): The media id of the airing schedule.
    media (str): The media schema of the airing schedule.
"""
