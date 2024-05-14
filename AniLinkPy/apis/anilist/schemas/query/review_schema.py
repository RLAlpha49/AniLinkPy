from AniLinkPy.apis.anilist.schemas.basic_schema import BASICUSERSCHEMA
from AniLinkPy.apis.anilist.schemas.query.media_schema import MEDIASCHEMA

REVIEWSCHEMA = f"""
  id
  mediaId
  userId
  mediaType
  summary
  body (asHtml: $asHtml)
  rating
  ratingAmount
  score
  private
  siteUrl
  createdAt
  updatedAt
  user {{
    {BASICUSERSCHEMA}
  }}
  media {{
    {MEDIASCHEMA}
  }}
"""

"""
ReviewSchema is a string representing the GraphQL schema for a review query. It includes the id, mediaId, userId,
mediaType, summary, body, rating, ratingAmount, score, private status, siteUrl, createdAt, updatedAt, user, and media.

Attributes:
    id (int): The id of the review.
    mediaId (int): The media id of the review.
    userId (int): The user id of the review.
    mediaType (str): The media type of the review.
    summary (str): The summary of the review.
    body (str): The body of the review.
    rating (int): The rating of the review.
    ratingAmount (int): The rating amount of the review.
    score (int): The score of the review.
    private (bool): The private status of the review.
    siteUrl (str): The site url of the review.
    createdAt (int): The created at timestamp of the review.
    updatedAt (int): The updated at timestamp of the review.
    user (str): The basic user schema of the review.
    media (str): The media schema of the review.
"""
