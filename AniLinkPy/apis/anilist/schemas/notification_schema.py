from AniLinkPy.apis.anilist.schemas.basic_schema import (
    BASICCOMMENTSCHEMA,
    BASICTHREADSCHEMA,
    BASICUSERSCHEMA,
)

THREADNOTIFICATIONSCHEMA = f"""
  id
  userId
  type
  commentId
  context
  createdAt
  thread {{
    {BASICTHREADSCHEMA}
  }}
  comment {{
    {BASICCOMMENTSCHEMA}
  }}
  user {{
    {BASICUSERSCHEMA}
  }}
"""

"""
This is the NotificationSchema for the AniList API. It defines the structure of the notification data that is
expected to be returned from the API.

Attributes:
    id (int): The id of the thread notification.
    userId (int): The user id associated with the thread notification.
    type (str): The type of the thread notification.
    commentId (int): The comment id associated with the thread notification.
    context (str): The context of the thread notification.
    createdAt (str): The creation time of the thread notification.
    thread (str): The thread associated with the thread notification.
    comment (str): The comment associated with the thread notification.
    user (str): The user associated with the thread notification.
"""
