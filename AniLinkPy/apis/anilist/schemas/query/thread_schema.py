from AniLinkPy.apis.anilist.schemas.basic_schema import BASICUSERSCHEMA
from AniLinkPy.apis.anilist.schemas.query.media_schema import MEDIASCHEMA

THREADSCHEMA = f"""
  id
  title
  body (asHtml: $asHtml)
  userId
  replyUserId
  replyCommentId
  replyCount
  viewCount
  isLocked
  isSticky
  isSubscribed
  likeCount
  isLiked
  repliedAt
  createdAt
  updatedAt
  user {{
    {BASICUSERSCHEMA}
  }}
  replyUser {{
    {BASICUSERSCHEMA}
  }}
  likes {{
    {BASICUSERSCHEMA}
  }}
  siteUrl
  categories {{
    id
    name
  }}
  mediaCategories {{
    {MEDIASCHEMA}
  }}
"""

"""
ThreadSchema is a string representing the GraphQL schema for a thread query. It includes the thread's id, title,
body, userId, replyUserId, replyCommentId, replyCount, viewCount, isLocked status, isSticky status, isSubscribed
status, likeCount, isLiked status, repliedAt, createdAt, updatedAt, user of type `BasicUser`, replyUser of type
`BasicUser`, likes of type `BasicUser[]`, siteUrl, categories, and mediaCategories of type `MediaResponse[]`.

Attributes:
    id (int): The id of the thread.
    title (str): The title of the thread.
    body (str): The body of the thread.
    userId (int): The user id of the thread.
    replyUserId (int): The reply user id of the thread.
    replyCommentId (int): The reply comment id of the thread.
    replyCount (int): The reply count of the thread.
    viewCount (int): The view count of the thread.
    isLocked (bool): The locked status of the thread.
    isSticky (bool): The sticky status of the thread.
    isSubscribed (bool): The subscribed status of the thread.
    likeCount (int): The like count of the thread.
    isLiked (bool): The liked status of the thread.
    repliedAt (int): The replied at timestamp of the thread.
    createdAt (int): The created at timestamp of the thread.
    updatedAt (int): The updated at timestamp of the thread.
    user (str): The basic user schema of the thread.
    replyUser (str): The basic user schema of the reply user of the thread.
    likes (str): The basic user schema of the likes of the thread.
    siteUrl (str): The site url of the thread.
    categories (str): The categories of the thread.
    mediaCategories (str): The media schema of the media categories of the thread.
"""
