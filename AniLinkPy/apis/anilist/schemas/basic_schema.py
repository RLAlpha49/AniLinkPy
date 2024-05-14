BASICUSERSCHEMA = """
  id
  name
  avatar {
    large
  }
"""

"""
This is the BasicUserSchema for the AniList API. It defines the structure of the image data that is expected to be
returned from the API.

Attributes:
    id (int): The id of the user.
    name (str): The name of the user.
    avatar (dict): The avatar of the user with a large size.
"""

BASICTHREADSCHEMA = """
  id
  title
  body (asHtml: $asHtml)
  siteUrl
"""

"""
This is the BasicThreadSchema for the AniList API. It defines the structure of the image data that is expected to be
returned from the API.

Attributes:
    id (int): The id of the thread.
    title (str): The title of the thread.
    body (str): The body of the thread.
    siteUrl (str): The site URL of the thread.
"""

BASICCOMMENTSCHEMA = """
  id
  userId
  threadId
"""

"""
This is the BasicCommentSchema for the AniList API. It defines the structure of the image data that is expected to be
returned from the API.

Attributes:
    id (int): The id of the comment.
    userId (int): The id of the user who made the comment.
    threadId (int): The id of the thread where the comment is.
"""
