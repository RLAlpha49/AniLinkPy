RANKINGSCHEMA = """
  rankings {
    id
    rank
    type
    format
    year
    season
    allTime
    context
  }
"""

"""
This is the RankingSchema for the AniList API. It defines the structure of the ranking data that is expected to be
returned from the API.

Attributes:
    id (int): The id of the ranking.
    rank (int): The rank of the ranking.
    type (str): The type of the ranking.
    format (str): The format of the ranking.
    year (int): The year of the ranking.
    season (str): The season of the ranking.
    allTime (bool): The all-time status of the ranking.
    context (str): The context of the ranking.
"""
