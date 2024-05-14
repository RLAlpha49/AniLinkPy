from AniLinkPy.apis.anilist.schemas.basic_schema import BASICUSERSCHEMA
from AniLinkPy.apis.anilist.schemas.query.media_schema import MEDIASCHEMA

RECOMMENDATIONSCHEMA = f"""
  id
  rating
  userRating
  media {{
    {MEDIASCHEMA}
  }}
  mediaRecommendation {{
    {MEDIASCHEMA}
  }}
  user {{
    {BASICUSERSCHEMA}
  }}
"""

"""
RecommendationSchema is a string representing the GraphQL schema for a recommendation query.
It includes the id, rating, user rating, media, media recommendation, and user.

Attributes:
    id (int): The id of the recommendation.
    rating (int): The rating of the recommendation.
    userRating (int): The user rating of the recommendation.
    media (str): The media schema of the recommendation.
    mediaRecommendation (str): The media recommendation schema of the recommendation.
    user (str): The basic user schema of the recommendation.
"""
