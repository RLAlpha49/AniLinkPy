from AniLinkPy.apis.anilist.schemas.activity_schema import ACTIVITYNOTIFICATIONSCHEMA
from AniLinkPy.apis.anilist.schemas.basic_schema import (
    BASICCOMMENTSCHEMA,
    BASICUSERSCHEMA,
)
from AniLinkPy.apis.anilist.schemas.notification_schema import THREADNOTIFICATIONSCHEMA
from AniLinkPy.apis.anilist.schemas.title_schema import TITLESCHEMA

NOTIFICATIONSCHEMA = f"""
  ... on AiringNotification {{
    id
    type
    animeId
    episode
    contexts
    createdAt
    media {{
      id
      {TITLESCHEMA}
    }}
  }}
  ... on FollowingNotification {{
    id
    type
    userId
    context
    createdAt
    user {{
      {BASICUSERSCHEMA}
    }}
  }}
  ... on ActivityMessageNotification {{
    id
    userId
    type
    activityId
    context
    createdAt
    message {{
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
      replies {{
        id
        userId
        activityId
        text (asHtml: $asHtml)
        createdAt
        likeCount
        isLiked
        user {{
          {BASICUSERSCHEMA}
        }}
        likes {{
          {BASICUSERSCHEMA}
        }}
      }}
      likes {{
        {BASICUSERSCHEMA}
      }}
    }}
    user {{
      {BASICUSERSCHEMA}
    }}
  }}
  ... on ActivityMentionNotification {{
    {ACTIVITYNOTIFICATIONSCHEMA}
  }}
  ... on ActivityReplyNotification {{
    {ACTIVITYNOTIFICATIONSCHEMA}
  }}
  ... on ActivityReplySubscribedNotification {{
    {ACTIVITYNOTIFICATIONSCHEMA}
  }}
  ... on ActivityLikeNotification {{
    {ACTIVITYNOTIFICATIONSCHEMA}
  }}
  ... on ActivityReplyLikeNotification {{
    {ACTIVITYNOTIFICATIONSCHEMA}
  }}
  ... on ThreadCommentMentionNotification {{
    {THREADNOTIFICATIONSCHEMA}
  }}
  ... on ThreadCommentReplyNotification {{
    {THREADNOTIFICATIONSCHEMA}
  }}
  ... on ThreadCommentSubscribedNotification {{
    {THREADNOTIFICATIONSCHEMA}
  }}
  ... on ThreadCommentLikeNotification {{
    {THREADNOTIFICATIONSCHEMA}
  }}
  ... on ThreadLikeNotification {{
    id
    userId
    type
    context
    createdAt
    thread {{
      ${{BasicThreadSchema}}
    }}
    comment {{
      {BASICCOMMENTSCHEMA}
    }}
    user {{
      {BASICUSERSCHEMA}
    }}
  }}
  ... on RelatedMediaAdditionNotification {{
    id
    type
    mediaId
    context
    createdAt
    media {{
      id
      {TITLESCHEMA}
    }}
  }}
  ... on MediaDataChangeNotification {{
    id
    type
    mediaId
    context
    reason
    createdAt
    media {{
      id
      {TITLESCHEMA}
    }}
  }}
  ... on MediaMergeNotification {{
    id
    type
    mediaId
    deletedMediaTitles
    context
    reason
    createdAt
    media {{
      id
      {TITLESCHEMA}
    }}
  }}
  ... on MediaDeletionNotification {{
    id
    type
    deletedMediaTitle
    context
    reason
    createdAt
  }}
"""

"""
NotificationSchema is a string representing the GraphQL schema for a notification query. It includes various types
of notifications such as AiringNotification, FollowingNotification, ActivityMessageNotification,
ActivityMentionNotification, ActivityReplyNotification, ActivityReplySubscribedNotification,
ActivityLikeNotification, ActivityReplyLikeNotification, ThreadCommentMentionNotification,
ThreadCommentReplyNotification, ThreadCommentSubscribedNotification, ThreadCommentLikeNotification,
ThreadLikeNotification, RelatedMediaAdditionNotification, MediaDataChangeNotification, MediaMergeNotification,
and MediaDeletionNotification.

Attributes:
    id (int): The id of the notification.
    type (str): The type of the notification.
    animeId (int): The anime id of the notification.
    episode (int): The episode of the notification.
    contexts (list): The contexts of the notification.
    createdAt (int): The created at timestamp of the notification.
    media (str): The media schema of the notification.
    userId (int): The user id of the notification.
    context (str): The context of the notification.
    user (str): The basic user schema of the notification.
    activityId (int): The activity id of the notification.
    message (str): The message of the notification.
    thread (str): The basic thread schema of the notification.
    comment (str): The basic comment schema of the notification.
    mediaId (int): The media id of the notification.
    reason (str): The reason of the notification.
    deletedMediaTitles (list): The deleted media titles of the notification.
    deletedMediaTitle (str): The deleted media title of the notification.
"""
