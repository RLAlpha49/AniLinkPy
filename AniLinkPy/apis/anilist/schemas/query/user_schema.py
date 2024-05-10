"""
This is the UserSchema for the Anilist API. It defines the structure of the user data that is expected to be
returned from the API.

Attributes:
    id (int): The user's ID.
    name (str): The user's name.
    about (str): The user's about information.
    avatar (dict): The user's avatar, with 'large' and 'medium' sizes.
    bannerImage (str): The URL of the user's banner image.
    isFollowing (bool): Whether the user is following.
    isFollower (bool): Whether the user is a follower.
    isBlocked (bool): Whether the user is blocked.
    bans (list): The user's bans.
    options (dict): The user's options.
    mediaListOptions (dict): The user's media list options.
    favourites (dict): The user's favourites.
    statistics (dict): The user's statistics.
    stats (dict): The user's stats.
    unreadNotificationCount (int): The user's unread notification count.
    siteUrl (str): The user's site URL.
    donatorTier (int): The user's donator tier.
    donatorBadge (str): The user's donator badge.
    moderatorRoles (list): The user's moderator roles.
    createdAt (int): The timestamp of when the user was created.
    updatedAt (int): The timestamp of when the user was last updated.
    previousNames (list): The user's previous names.
"""

from AniLinkPy.apis.anilist.schemas.cover_image_schema import COVERIMAGESCHEMA
from AniLinkPy.apis.anilist.schemas.image_schema import IMAGESCHEMA
from AniLinkPy.apis.anilist.schemas.name_schema import NAMESCHEMA
from AniLinkPy.apis.anilist.schemas.tag_schema import TAGSCHEMA
from AniLinkPy.apis.anilist.schemas.title_schema import TITLESCHEMA
from AniLinkPy.apis.anilist.schemas.user_stats_schema import (
    USERANIMESTATSSCHEMA,
    USERMANGASTATSSCHEMA,
)

UserSchema = f"""
  id
  name
  about(asHtml: $asHtml)
  avatar {{
    large
    medium
  }}
  bannerImage
  isFollowing
  isFollower
  isBlocked
  bans
  options {{
    titleLanguage
    displayAdultContent
    airingNotifications
    profileColor
    notificationOptions {{
      type
      enabled
    }}
    timezone
    activityMergeTime
    staffNameLanguage
    restrictMessagesToFollowing
    disabledListActivity {{
    disabled
    type
    }}
  }}
  mediaListOptions {{
    scoreFormat
    rowOrder
    animeList {{
      sectionOrder
      splitCompletedSectionByFormat
      customLists
      advancedScoring
      advancedScoringEnabled
    }}
    mangaList {{
      sectionOrder
      splitCompletedSectionByFormat
      customLists
      advancedScoring
      advancedScoringEnabled
    }}
  }}
  favourites {{
    anime (perPage: 50) {{
      edges {{
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
    manga (perPage: 50) {{
      edges {{
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
    characters (perPage: 50) {{
      edges {{
        id
        role
        name
        voiceActors {{
          id
          {NAMESCHEMA}
          {IMAGESCHEMA}
        }}
        media {{
          id
          {TITLESCHEMA}
          {COVERIMAGESCHEMA}
        }}
        favouriteOrder
        node {{
          id
          {NAMESCHEMA}
          {IMAGESCHEMA}
        }}
      }}
    }}
    staff (perPage: 50) {{
      edges {{
        id
        role
        favouriteOrder
        node {{
          id
          {NAMESCHEMA}
          {IMAGESCHEMA}
        }}
      }}
    }}
    studios (perPage: 50) {{
      edges {{
        id
        isMain
        favouriteOrder
        node {{
          id
          name
          isAnimationStudio
          siteUrl
        }}
      }}
    }}
  }}
  statistics {{
    anime {{
      count
      meanScore
      standardDeviation
      minutesWatched
      episodesWatched
      formats (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        format
      }}
      statuses (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        status
      }}
      scores (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        score
      }}
      lengths (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        length
      }}
      releaseYears (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        releaseYear
      }}
      startYears (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        startYear
      }}
      genres (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        genre
      }}
      tags (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        tag {{
          {TAGSCHEMA}
        }}
      }}
      countries (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        country
      }}
      voiceActors (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        voiceActor {{
          id
          {NAMESCHEMA}
        }}
        characterIds
      }}
      staff (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        staff {{
          id
          {NAMESCHEMA}
        }}
      }}
      studios (limit: $animeStatLimit, sort: $animeStatSort) {{
        {USERANIMESTATSSCHEMA}
        studio {{
          id
          name
        }}
      }}
    }}
    manga {{
      count
      meanScore
      standardDeviation
      chaptersRead
      volumesRead
      formats (limit: $mangaStatLimit, sort: $mangaStatSort) {{
        {USERMANGASTATSSCHEMA}
        format
      }}
      statuses (limit: $mangaStatLimit, sort: $mangaStatSort) {{
        {USERMANGASTATSSCHEMA}
        status
      }}
      scores (limit: $mangaStatLimit, sort: $mangaStatSort) {{
        {USERMANGASTATSSCHEMA}
        score
      }}
      lengths (limit: $mangaStatLimit, sort: $mangaStatSort) {{
        {USERMANGASTATSSCHEMA}
        length
      }}
      releaseYears (limit: $mangaStatLimit, sort: $mangaStatSort) {{
        {USERMANGASTATSSCHEMA}
        releaseYear
      }}
      startYears (limit: $mangaStatLimit, sort: $mangaStatSort) {{
        {USERMANGASTATSSCHEMA}
        startYear
      }}
      genres (limit: $mangaStatLimit, sort: $mangaStatSort) {{
        {USERMANGASTATSSCHEMA}
        genre
      }}
      tags (limit: $mangaStatLimit, sort: $mangaStatSort) {{
        {USERMANGASTATSSCHEMA}
        tag {{
          {TAGSCHEMA}
        }}
      }}
      countries (limit: $mangaStatLimit, sort: $mangaStatSort) {{
        {USERMANGASTATSSCHEMA}
        country
      }}
      staff (limit: $mangaStatLimit, sort: $mangaStatSort) {{
        {USERMANGASTATSSCHEMA}
        staff {{
          id
          {NAMESCHEMA}
        }}
      }}
      studios (limit: $mangaStatLimit, sort: $mangaStatSort) {{
        {USERMANGASTATSSCHEMA}
        studio {{
          id
          name
        }}
      }}
    }}
  }}
  stats {{
    watchedTime
    chaptersRead
    activityHistory {{
      date
      amount
      level
    }}
    animeStatusDistribution {{
      status
      amount
    }}
    mangaStatusDistribution {{
      status
      amount
    }}
    animeScoreDistribution {{
      score
      amount
    }}
    mangaScoreDistribution {{
      score
      amount
    }}
    animeListScores {{
      meanScore
      standardDeviation
    }}
    mangaListScores {{
      meanScore
      standardDeviation
    }}
    favouredGenresOverview {{
      genre
      amount
      meanScore
      timeWatched
    }}
    favouredGenres {{
      genre
      amount
      meanScore
      timeWatched
    }}
    favouredTags {{
      tag {{
        {TAGSCHEMA}
      }}
      amount
      meanScore
      timeWatched
    }}
    favouredActors {{
      staff {{
        id
        {NAMESCHEMA}
      }}
      amount
      meanScore
      timeWatched
    }}
    favouredStaff {{
      staff {{
        id
        {NAMESCHEMA}
      }}
      amount
      meanScore
      timeWatched
    }}
    favouredStudios {{
      studio {{
        id
        name
      }}
      amount
      meanScore
      timeWatched
    }}
    favouredYears {{
      year
      amount
      meanScore
    }}
    favouredFormats {{
      format
      amount
    }}
  }}
  unreadNotificationCount
  siteUrl
  donatorTier
  donatorBadge
  moderatorRoles
  createdAt
  updatedAt
  previousNames {{
    name
    createdAt
    updatedAt
  }}
"""
