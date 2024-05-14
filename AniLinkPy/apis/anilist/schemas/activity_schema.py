from AniLinkPy.apis.anilist.schemas.basic_schema import BASICUSERSCHEMA
from AniLinkPy.apis.anilist.schemas.title_schema import TITLESCHEMA

ACTIVITYREPLYSCHEMA = f"""
  id
  userId
  activityId
  text (asHtml: $asHtml)
  likeCount
  isLiked
  createdAt
  user {{
    {BASICUSERSCHEMA}
  }}
  likes {{
    {BASICUSERSCHEMA}
  }}
"""

"""
This is the ActivityReplySchema for the Anilist API. It defines the structure of the activity reply data.

Attributes:
    id (int): The id of the activity.
    userId (int): The id of the user who created the activity.
    activityId (int): The id of the activity.
    text (str): The text of the activity.
    likeCount (int): The count of likes on the activity.
    isLiked (bool): Whether the activity is liked by the user.
    createdAt (int): The timestamp when the activity was created.
    user (BasicUser): The user who created the activity.
    likes (list): The list of users who liked the activity.
"""

ACTIVITYSCHEMA = """
  activity {
    ... on TextActivity {
      id
      userId
      type
      replyCount
      text (asHtml: $asHtml)
      siteUrl
      isLocked
      isSubscribed
      likeCount
      isLiked
      isPinned
      createdAt
    }
    ... on ListActivity {
      id
      userId
      type
      replyCount
      status
      progress
      isLocked
      isSubscribed
      likeCount
      isLiked
      isPinned
      siteUrl
      createdAt
      media {
        id
        title {
          romaji
          english
        }
      }
    }
    ... on MessageActivity {
      id
      recipientId
      messengerId
      type
      replyCount
      message (asHtml: $asHtml)
      isLocked
      isSubscribed
      likeCount
      isLiked
      isPrivate
      siteUrl
      createdAt
    }
  }
"""

"""
This is the ActivitySchema for the Anilist API. It defines the structure of the activity data

Attributes:
    id (int): The id of the activity.
    userId (int): The id of the user who created the activity.
    type (str): The type of the activity.
    replyCount (int): The count of replies on the activity.
    text (str): The text of the activity.
    siteUrl (str): The site URL of the activity.
    isLocked (bool): Whether the activity is locked.
    isSubscribed (bool): Whether the user is subscribed to the activity.
    likeCount (int): The count of likes on the activity.
    isLiked (bool): Whether the activity is liked by the user.
    isPinned (bool): Whether the activity is pinned.
    createdAt (int): The timestamp when the activity was created.
"""

ACTIVITYSCHEMAV2 = f"""
  activity {{
    ... on TextActivity {{
      id
      userId
      type
      replyCount
      text (asHtml: $asHtml)
      siteUrl
      isLocked
      isSubscribed
      likeCount
      isLiked
      isPinned
      createdAt
      user {{
        {BASICUSERSCHEMA}
      }}
      replies {{
        {ACTIVITYREPLYSCHEMA}
      }}
      likes {{
        {BASICUSERSCHEMA}
      }}
    }}
    ... on ListActivity {{
      id
      userId
      type
      replyCount
      status
      progress
      isLocked
      isSubscribed
      likeCount
      isLiked
      isPinned
      siteUrl
      createdAt
      media {{
        id
        title {{
          romaji
          english
        }}
      }}
      user {{
        {BASICUSERSCHEMA}
      }}
      replies {{
        {ACTIVITYREPLYSCHEMA}
      }}
      likes {{
        {BASICUSERSCHEMA}
      }}
    }}
    ... on MessageActivity {{
      id
      recipientId
      messengerId
      type
      replyCount
      message (asHtml: $asHtml)
      isLocked
      isSubscribed
      likeCount
      isLiked
      isPrivate
      siteUrl
      createdAt
      recipient {{
        {BASICUSERSCHEMA}
      }}
      messenger {{
        {BASICUSERSCHEMA}
      }}
      replies {{
        {ACTIVITYREPLYSCHEMA}
      }}
      likes {{
        {BASICUSERSCHEMA}
      }}
    }}
    ... on ActivityReply {{
      id
      userId
      activityId
      text (asHtml: $asHtml)
      likeCount
      isLiked
      createdAt
      user {{
        {BASICUSERSCHEMA}
      }}
      likes {{
        {BASICUSERSCHEMA}
      }}
    }}
    ... on Thread {{
      id
      title
      body (asHtml: $asHtml)
      ThreadUserId: userId
      replyUserId
      replyCommentId
      ThreadReplyCount: replyCount
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
        id
        {TITLESCHEMA}
      }}
    }}
    ... on ThreadComment {{
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
        id
        title
      }}
      user {{
        {BASICUSERSCHEMA}
      }}
      likes {{
        {BASICUSERSCHEMA}
      }}
      childComments
      isLocked
    }}
  }}
"""

"""
This is the ActivitySchemaV2 for the Anilist API. It defines the structure of the activity data

Attributes:
    id (int): The id of the activity.
    userId (int): The id of the user who created the activity.
    type (str): The type of the activity.
    replyCount (int): The count of replies on the activity.
    text (str): The text of the activity.
    siteUrl (str): The site URL of the activity.
    isLocked (bool): Whether the activity is locked.
    isSubscribed (bool): Whether the user is subscribed to the activity.
    likeCount (int): The count of likes on the activity.
    isLiked (bool): Whether the activity is liked by the user.
    isPinned (bool): Whether the activity is pinned.
    createdAt (int): The timestamp when the activity was created.
    user (BasicUser): The user who created the activity.
    replies (list): The list of replies to the activity.
    likes (list): The list of users who liked the activity.
"""

ACTIVITYWITHREPLIESSCHEMA = f"""
  activity {{
    ... on TextActivity {{
      id
      userId
      type
      replyCount
      text (asHtml: $asHtml)
      siteUrl
      isLocked
      isSubscribed
      likeCount
      isLiked
      isPinned
      createdAt
      user {{
        {BASICUSERSCHEMA}
      }}
      replies {{
        {ACTIVITYREPLYSCHEMA}
      }}
      likes {{
        {BASICUSERSCHEMA}
      }}
    }}
    ... on ListActivity {{
      id
      userId
      type
      replyCount
      status
      progress
      isLocked
      isSubscribed
      likeCount
      isLiked
      isPinned
      siteUrl
      createdAt
      media {{
        id
        title {{
          romaji
          english
        }}
      }}
      user {{
        {BASICUSERSCHEMA}
      }}
      replies {{
        {ACTIVITYREPLYSCHEMA}
      }}
      likes {{
        {BASICUSERSCHEMA}
      }}
    }}
    ... on MessageActivity {{
      id
      recipientId
      messengerId
      type
      replyCount
      message (asHtml: $asHtml)
      isLocked
      isSubscribed
      likeCount
      isLiked
      isPrivate
      siteUrl
      createdAt
      recipient {{
        BASICUSERSCHEMA
      }}
      messenger {{
        {BASICUSERSCHEMA}
      }}
      replies {{
        {ACTIVITYREPLYSCHEMA}
      }}
      likes {{
        {BASICUSERSCHEMA}
      }}
    }}
  }}
"""

"""
This is the ActivityWithRepliesSchema for the Anilist API. It defines the structure of the activity data

Attributes:
    id (int): The id of the activity.
    userId (int): The id of the user who created the activity.
    type (str): The type of the activity.
    replyCount (int): The count of replies on the activity.
    text (str): The text of the activity.
    siteUrl (str): The site URL of the activity.
    isLocked (bool): Whether the activity is locked.
    isSubscribed (bool): Whether the user is subscribed to the activity.
    likeCount (int): The count of likes on the activity.
    isLiked (bool): Whether the activity is liked by the user.
    isPinned (bool): Whether the activity is pinned.
    createdAt (int): The timestamp when the activity was created.
    user (BasicUser): The user who created the activity.
    replies (list): The list of replies to the activity.
    likes (list): The list of users who liked the activity.
"""

TEXTACTIVITYSCHEMA = f"""
  id
  userId
  type
  replyCount
  text (asHtml: $asHtml)
  siteUrl
  isLocked
  isSubscribed
  likeCount
  isLiked
  isPinned
  createdAt
  user {{
    {BASICUSERSCHEMA}
  }}
  replies {{
    {ACTIVITYREPLYSCHEMA}
  }}
  likes {{
    {BASICUSERSCHEMA}
  }}
"""

"""
This is the TextActivitySchema for the Anilist API. It defines the structure of the text activity data.

Attributes:
    id (int): The id of the text activity.
    userId (int): The id of the user who created the text activity.
    type (str): The type of the text activity.
    replyCount (int): The count of replies on the text activity.
    text (str): The text of the text activity.
    siteUrl (str): The site URL of the text activity.
    isLocked (bool): Whether the text activity is locked.
    isSubscribed (bool): Whether the user is subscribed to the text activity.
    likeCount (int): The count of likes on the text activity.
    isLiked (bool): Whether the text activity is liked by the user.
    isPinned (bool): Whether the text activity is pinned.
    createdAt (int): The timestamp when the text activity was created.
    user (BasicUser): The user who created the text activity.
    replies (list): The list of replies to the text activity.
    likes (list): The list of users who liked the text activity.
"""

LISTACTIVITYSCHEMA = f"""
  id
  userId
  type
  replyCount
  status
  progress
  isLocked
  isSubscribed
  likeCount
  isLiked
  isPinned
  siteUrl
  createdAt
  media {{
    id
    title {{
      romaji
      english
    }}
  }}
  user {{
    {BASICUSERSCHEMA}
  }}
  replies {{
    {ACTIVITYREPLYSCHEMA}
  }}
  likes {{
    {BASICUSERSCHEMA}
  }}
"""

"""
This is the ListActivitySchema for the Anilist API. It defines the structure of the list activity data.

Attributes:
    id (int): The id of the list activity.
    userId (int): The id of the user who created the list activity.
    type (str): The type of the list activity.
    replyCount (int): The count of replies on the list activity.
    status (str): The status of the list activity.
    progress (int): The progress of the list activity.
    isLocked (bool): Whether the list activity is locked.
    isSubscribed (bool): Whether the user is subscribed to the list activity.
    likeCount (int): The count of likes on the list activity.
    isLiked (bool): Whether the list activity is liked by the user.
    isPinned (bool): Whether the list activity is pinned.
    siteUrl (str): The site URL of the list activity.
    createdAt (int): The timestamp when the list activity was created.
    media (dict): The media details of the list activity.
    user (BasicUser): The user who created the list activity.
    replies (list): The list of replies to the list activity.
    likes (list): The list of users who liked the list activity.
"""

MESSAGEACTIVITYSCHEMA = f"""
  id
  recipientId
  messengerId
  type
  replyCount
  message (asHtml: $asHtml)
  isLocked
  isSubscribed
  likeCount
  isLiked
  isPrivate
  siteUrl
  createdAt
  recipient {{
    {BASICUSERSCHEMA}
  }}
  messenger {{
    {BASICUSERSCHEMA}
  }}
  replies {{
    {ACTIVITYREPLYSCHEMA}
  }}
  likes {{
    {BASICUSERSCHEMA}
  }}
"""

"""
This is the MessageActivitySchema for the Anilist API. It defines the structure of the message activity data.

Attributes:
    id (int): The id of the message activity.
    recipientId (int): The id of the recipient of the message activity.
    messengerId (int): The id of the messenger of the message activity.
    type (str): The type of the message activity.
    replyCount (int): The count of replies on the message activity.
    message (str): The message of the message activity.
    isLocked (bool): Whether the message activity is locked.
    isSubscribed (bool): Whether the user is subscribed to the message activity.
    likeCount (int): The count of likes on the message activity.
    isLiked (bool): Whether the message activity is liked by the user.
    isPrivate (bool): Whether the message activity is private.
    siteUrl (str): The site URL of the message activity.
    createdAt (int): The timestamp when the message activity was created.
    recipient (BasicUser): The recipient of the message activity.
    messenger (BasicUser): The messenger of the message activity.
    replies (list): The list of replies to the message activity.
    likes (list): The list of users who liked the message activity.
"""

ACTIVITYNOTIFICATIONSCHEMA = f"""
  id
  userId
  type
  activityId
  context
  createdAt
  {ACTIVITYSCHEMA}
    user {{
      {BASICUSERSCHEMA}
    }}
"""

"""
This is the ActivityNotificationSchema for the Anilist API. It defines the structure of the activity notification data.

Attributes:
    id (int): The id of the notification.
    userId (int): The id of the user who created the notification.
    type (str): The type of the notification.
    activityId (int): The id of the activity related to the notification.
    context (str): The context of the notification.
    createdAt (int): The timestamp when the notification was created.
    ActivitySchema (str): The details of the activity related to the notification.
    BASICUSERSCHEMA (str): The details of the user who created the notification.
"""
