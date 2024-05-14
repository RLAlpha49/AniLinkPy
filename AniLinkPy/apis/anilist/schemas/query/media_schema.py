from AniLinkPy.apis.anilist.schemas.cover_image_schema import COVERIMAGESCHEMA
from AniLinkPy.apis.anilist.schemas.distribution_schema import (
    SCOREDISTRIBUTIONSCHEMA,
    STATUSDISTRIBUTIONSCHEMA,
)
from AniLinkPy.apis.anilist.schemas.external_link_schema import EXTERNALLINKSCHEMA
from AniLinkPy.apis.anilist.schemas.fuzzy_date_schema import FUZZYDATESCHEMA
from AniLinkPy.apis.anilist.schemas.media_list_entry_schema import MEDIALISTENTRYSCHEMA
from AniLinkPy.apis.anilist.schemas.next_airing_episode_schema import (
    NEXTAIRINGEPISODESCHEMA,
)
from AniLinkPy.apis.anilist.schemas.ranking_schema import RANKINGSCHEMA
from AniLinkPy.apis.anilist.schemas.streaming_episode_schema import (
    STREAMINGEPISODESCHEMA,
)
from AniLinkPy.apis.anilist.schemas.tag_schema import TAGSCHEMA
from AniLinkPy.apis.anilist.schemas.title_schema import TITLESCHEMA
from AniLinkPy.apis.anilist.schemas.trailer_schema import TRAILERSCHEMA

MEDIASCHEMA = f"""
  id
  idMal
  {TITLESCHEMA}
  type
  format
  status
  description (asHtml: $asHtml)
  startDate {{
    {FUZZYDATESCHEMA}
  }}
  endDate {{
    {FUZZYDATESCHEMA}
  }}
  season
  seasonYear
  seasonInt
  episodes
  duration
  chapters
  volumes
  countryOfOrigin
  isLicensed
  source
  hashtag
  {TRAILERSCHEMA}
  updatedAt
  {COVERIMAGESCHEMA}
  bannerImage
  genres
  synonyms
  averageScore
  meanScore
  popularity
  isLocked
  trending
  favourites
  tags {{
    {TAGSCHEMA}
  }}
  isFavourite
  isAdult
  {NEXTAIRINGEPISODESCHEMA}
  {EXTERNALLINKSCHEMA}
  {STREAMINGEPISODESCHEMA}
  {RANKINGSCHEMA}
  {MEDIALISTENTRYSCHEMA}
  stats {{
    {STATUSDISTRIBUTIONSCHEMA}
    {SCOREDISTRIBUTIONSCHEMA}
  }}
  siteUrl
  autoCreateForumThread
  isRecommendationBlocked
  modNotes
"""

"""
This is the MediaSchema for the AniList API. It defines the structure of the media data that is expected to be
returned from the API.

Attributes:
    id (int): The media's ID.
    idMal (int): The media's ID on MyAnimeList.
    title (dict): The media's title, with 'romaji', 'english', and 'native' versions.
    type (str): The type of the media (e.g., ANIME or MANGA).
    format (str): The format of the media (e.g., TV, TV_SHORT, MOVIE, SPECIAL, OVA, ONA, MUSIC, MANGA, NOVEL, ONE_SHOT).
    status (str): The status of the media (e.g., FINISHED, RELEASING, NOT_YET_RELEASED, CANCELLED).
    description (str): The media's description.
    startDate (dict): The media's start date, with 'year', 'month', and 'day'.
    endDate (dict): The media's end date, with 'year', 'month', and 'day'.
    season (str): The media's season (e.g., WINTER, SPRING, SUMMER, FALL).
    seasonYear (int): The year of the media's season.
    seasonInt (int): The integer representation of the media's season.
    episodes (int): The number of episodes in the media.
    duration (int): The duration of each episode in the media.
    chapters (int): The number of chapters in the media.
    volumes (int): The number of volumes in the media.
    countryOfOrigin (str): The country of origin of the media.
    isLicensed (bool): Whether the media is licensed.
    source (str): The source of the media (e.g., ORIGINAL, MANGA, LIGHT_NOVEL, VISUAL_NOVEL, VIDEO_GAME, OTHER).
    hashtag (str): The media's hashtag.
    updatedAt (int): The timestamp of when the media was last updated.
    coverImage (dict): The media's cover image, with 'extraLarge', 'large', 'medium', and 'color' versions.
    bannerImage (str): The URL of the media's banner image.
    genres (list): The media's genres.
    synonyms (list): The media's synonyms.
    averageScore (int): The media's average score.
    meanScore (int): The media's mean score.
    popularity (int): The media's popularity.
    isLocked (bool): Whether the media is locked.
    trending (int): The media's trending rank.
    favourites (int): The number of users who have the media in their favourites.
    tags (list): The media's tags.
    isFavourite (bool): Whether the media is a favourite.
    isAdult (bool): Whether the media is for adults.
    nextAiringEpisode (dict): The media's next airing episode, with 'airingAt', 'timeUntilAiring', and 'episode'.
    externalLinks (list): The media's external links.
    streamingEpisodes (list): The media's streaming episodes.
    rankings (list): The media's rankings.
    mediaListEntry (dict): The media's list entry.
    stats (dict): The media's stats.
    siteUrl (str): The media's site URL.
    autoCreateForumThread (bool): Whether a forum thread is automatically created for the media.
    isRecommendationBlocked (bool): Whether recommendation is blocked for the media.
    modNotes (str): The moderator's notes for the media.
"""
