from AniLinkPy.apis.anilist.schemas.basic_schema import BASICUSERSCHEMA
from AniLinkPy.apis.anilist.schemas.query.thread_schema import THREADSCHEMA

THREADCOMMENTSCHEMA = f"""
  id
  userId
  threadId
  comment (asHtml: $asHtml)
  likeCount
  isLiked
  siteUrl
  createdAt
  updatedAt
  thread {{
    {THREADSCHEMA}
  }}
  user {{
    {BASICUSERSCHEMA}
  }}
  likes {{
    {BASICUSERSCHEMA}
  }}
  childComments
  isLocked
"""

"""
ThreadCommentSchema is a string representing the GraphQL schema for a thread comment query. It includes the
comment's id, userId, threadId, comment, likeCount, isLiked status, siteUrl, createdAt, updatedAt, thread of type
`ThreadResponse`, user of type `BasicUser`, likes of type `BasicUser[]`, childComments, and isLocked status.

Attributes:
    id (int): The id of the thread comment.
    userId (int): The user id of the thread comment.
    threadId (int): The thread id of the thread comment.
    comment (str): The comment of the thread comment.
    likeCount (int): The like count of the thread comment.
    isLiked (bool): The liked status of the thread comment.
    siteUrl (str): The site url of the thread comment.
    createdAt (int): The created at timestamp of the thread comment.
    updatedAt (int): The updated at timestamp of the thread comment.
    thread (str): The thread schema of the thread comment.
    user (str): The basic user schema of the thread comment.
    likes (str): The basic user schema of the likes of the thread comment.
    childComments (str): The child comments of the thread comment.
    isLocked (bool): The locked status of the thread comment.
"""
