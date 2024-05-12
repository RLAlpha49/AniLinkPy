# AniList API

## Structure

AniLink for AniList is divided into two main sections: `anilist.query` and `anilist.mutation`. The `anilist.query` section contains methods for querying data from the AniList API, while the `anilist.mutation` section contains methods for mutating data.

### Custom Queries and Mutations

If needed there is a custom section `anilist.custom` that allows the user to pass a custom query or mutation to the AniList API.

The method accepts two parameters: the query or mutation string and an optional variables object.

!!! example "Custom Query"

    ```python
    viewer = aniLink.anilist.custom('query {Viewer {id}}')
    
    mutation = 'mutation ($about: String) {UpdateUser (about: $about) {id}}'
    variables = { 'about': "New about text" }
    response = aniLink.anilist.custom(mutation, variables)
    ```

### Query Methods

The `anilist.query` section is further divided into main query methods and page query methods. The main query methods return a single piece of data, while the page query methods return pages of data.

List of main query methods in `anilist.query`:

| Method                                                                                  | Description               | Example                                                 |
|-----------------------------------------------------------------------------------------|---------------------------|---------------------------------------------------------|
| [user](AniLink/AniList/Queries/user.md)                                                 | Get a user                | `aniLink.anilist.query.user({'id': 542244})`            |
| [media](AniLink/AniList/Queries/media.md)                                               | Get a media               | `aniLink.anilist.query.media({'id': 1})`                |
| [mediaTrend](AniLink/AniList/Queries/mediaTrend.md)                                     | Get media trends          | `aniLink.anilist.query.mediaTrend({'mediaId': 1})`      |
| [airingSchedule](AniLink/AniList/Queries/airingSchedule.md)                             | Get airing schedule       | `aniLink.anilist.query.airingSchedule()`                |
| [character](AniLink/AniList/Queries/character.md)                                       | Get a character           | `aniLink.anilist.query.character({'id': 1})`            |
| [staff](AniLink/AniList/Queries/staff.md)                                               | Get a staff               | `aniLink.anilist.query.staff({'id': 1})`                |
| [mediaList](AniLink/AniList/Queries/mediaList.md)                                       | Get a media list          | `aniLink.anilist.query.mediaList({'id': 1})`            |
| [mediaListCollection](AniLink/AniList/Queries/mediaListCollection.md)                   | Get media list collection | `aniLink.anilist.query.mediaListCollection()`           |
| [genreCollection](AniLink/AniList/Queries/genreCollection.md)                           | Get genre collection      | `aniLink.anilist.query.genreCollection()`               |
| [mediaTagCollection](AniLink/AniList/Queries/mediaTagCollection.md)                     | Get media tag collection  | `aniLink.anilist.query.mediaTagCollection()`            |
| [viewer](AniLink/AniList/Queries/viewer.md)                                             | Get the current viewer    | `aniLink.anilist.query.viewer()`                        |
| [notification](AniLink/AniList/Queries/notification.md)                                 | Get notifications         | `aniLink.anilist.query.notification()`                  |
| [studio](AniLink/AniList/Queries/studio.md)                                             | Get a studio              | `aniLink.anilist.query.studio({'id': 1})`               |
| [review](AniLink/AniList/Queries/review.md)                                             | Get a review              | `aniLink.anilist.query.review({'id': 1})`               |
| [activity](AniLink/AniList/Queries/activity.md)                                         | Get an activity           | `aniLink.anilist.query.activity({'id': 1})`             |
| [activityReply](AniLink/AniList/Queries/activityReply.md)                               | Get an activity reply     | `aniLink.anilist.query.activityReply({'id': 1})`        |
| [following](AniLink/AniList/Queries/following.md)                                       | Get following users       | `aniLink.anilist.query.following()`                     |
| [follower](AniLink/AniList/Queries/follower.md)                                         | Get follower users        | `aniLink.anilist.query.follower()`                      |
| [thread](AniLink/AniList/Queries/thread.md)                                             | Get a thread              | `aniLink.anilist.query.thread({'id': 1})`               |
| [threadComment](AniLink/AniList/Queries/threadComment.md)                               | Get a thread comment      | `aniLink.anilist.query.threadComment({'id': 1})`        |
| [recommendation](AniLink/AniList/Queries/recommendation.md)                             | Get a recommendation      | `aniLink.anilist.query.recommendation({'id': 1})`       |
| [markdown](AniLink/AniList/Queries/markdown.md)                                         | Get markdown              | `aniLink.anilist.query.markdown({'markdown': 'Hello'})` |
| [aniChartUser](AniLink/AniList/Queries/aniChartUser.md)                                 | Get AniChart user         | `aniLink.anilist.query.aniChartUser({'id': 1})`         |
| [siteStatistics](AniLink/AniList/Queries/siteStatistics.md)                             | Get site statistics       | `aniLink.anilist.query.siteStatistics()`                |
| [externalLinkSourceCollection](AniLink/AniList/Queries/externalLinkSourceCollection.md) | Get external link sources | `aniLink.anilist.query.externalLinkSourceCollection()`  |

List of page query methods in `anilist.query.page`:

| Method                                                             | Description          | Example                                                   |
|--------------------------------------------------------------------|----------------------|-----------------------------------------------------------|
| [users](AniLink/AniList/Queries/Page/users.md)                     | Get users            | `aniLink.anilist.query.page.users({'page': 1})`           |
| [medias](AniLink/AniList/Queries/Page/medias.md)                   | Get medias           | `aniLink.anilist.query.page.medias({'page': 1})`          |
| [characters](AniLink/AniList/Queries/Page/characters.md)           | Get characters       | `aniLink.anilist.query.page.characters({'page': 1})`      |
| [staffs](AniLink/AniList/Queries/Page/staffs.md)                   | Get staffs           | `aniLink.anilist.query.page.staffs({'page': 1})`          |
| [studios](AniLink/AniList/Queries/Page/studios.md)                 | Get studios          | `aniLink.anilist.query.page.studios({'page': 1})`         |
| [mediaLists](AniLink/AniList/Queries/Page/mediaLists.md)           | Get media lists      | `aniLink.anilist.query.page.mediaLists({'page': 1})`      |
| [airingSchedules](AniLink/AniList/Queries/Page/airingSchedules.md) | Get airing schedules | `aniLink.anilist.query.page.airingSchedules({'page': 1})` |
| [mediaTrends](AniLink/AniList/Queries/Page/mediaTrends.md)         | Get media trends     | `aniLink.anilist.query.page.mediaTrends({'page': 1})`     |
| [notifications](AniLink/AniList/Queries/Page/notifications.md)     | Get notifications    | `aniLink.anilist.query.page.notifications({'page': 1})`   |
| [followers](AniLink/AniList/Queries/Page/followers.md)             | Get followers        | `aniLink.anilist.query.page.followers({'page': 1})`       |
| [following](AniLink/AniList/Queries/Page/following.md)             | Get following users  | `aniLink.anilist.query.page.following({'page': 1})`       |
| [activities](AniLink/AniList/Queries/Page/activities.md)           | Get activities       | `aniLink.anilist.query.page.activities({'page': 1})`      |
| [activityReplies](AniLink/AniList/Queries/Page/activityReplies.md) | Get activity replies | `aniLink.anilist.query.page.activityReplies({'page': 1})` |
| [threads](AniLink/AniList/Queries/Page/threads.md)                 | Get threads          | `aniLink.anilist.query.page.threads({'page': 1})`         |
| [threadComments](AniLink/AniList/Queries/Page/threadComments.md)   | Get thread comments  | `aniLink.anilist.query.page.threadComments({'page': 1})`  |
| [reviews](AniLink/AniList/Queries/Page/reviews.md)                 | Get reviews          | `aniLink.anilist.query.page.reviews({'page': 1})`         |
| [recommendations](AniLink/AniList/Queries/Page/recommendations.md) | Get recommendations  | `aniLink.anilist.query.page.recommendations({'page': 1})` |
| [likes](AniLink/AniList/Queries/Page/likes.md)                     | Get likes            | `aniLink.anilist.query.page.likes({'page': 1})`           |

### Mutation Methods

List of methods in `anilist.mutation`:

| Method                                                                                | Description                  | Example                                                                                      |
|---------------------------------------------------------------------------------------|------------------------------|----------------------------------------------------------------------------------------------|
| [updateUser](AniLink/AniList/Mutations/updateUser.md)                                 | Update a user                | `aniLink.anilist.mutation.updateUser({'about': 'New about text'})`                           |
| [saveMediaListEntry](AniLink/AniList/Mutations/saveMediaListEntry.md)                 | Save a media list entry      | `aniLink.anilist.mutation.saveMediaListEntry({'mediaId': 1, 'status': 'COMPLETED'})`         |
| [updateMediaListEntries](AniLink/AniList/Mutations/updateMediaListEntries.md)         | Update media list entries    | `aniLink.anilist.mutation.updateMediaListEntries({'mediaId': 1, 'status': 'COMPLETED'})`     |
| [deleteMediaListEntries](AniLink/AniList/Mutations/deleteMediaListEntries.md)         | Delete media list entries    | `aniLink.anilist.mutation.deleteMediaListEntries({'ids': [1, 2, 3]})`                        |
| [deleteCustomLists](AniLink/AniList/Mutations/deleteCustomLists.md)                   | Delete custom lists          | `aniLink.anilist.mutation.deleteCustomLists({'ids': [1, 2, 3]})`                             |
| [saveTextActivity](AniLink/AniList/Mutations/saveTextActivity.md)                     | Save a text activity         | `aniLink.anilist.mutation.saveTextActivity({'text': 'Hello'})`                               |
| [saveMessageActivity](AniLink/AniList/Mutations/saveMessageActivity.md)               | Save a message activity      | `aniLink.anilist.mutation.saveMessageActivity({'message': 'Hello'})`                         |
| [deleteActivity](AniLink/AniList/Mutations/deleteActivity.md)                         | Delete an activity           | `aniLink.anilist.mutation.deleteActivity({'id': 1})`                                         |
| [toggleActivityPin](AniLink/AniList/Mutations/toggleActivityPin.md)                   | Toggle activity pin          | `aniLink.anilist.mutation.toggleActivityPin({'id': 1})`                                      |
| [toggleActivitySubscription](AniLink/AniList/Mutations/toggleActivitySubscription.md) | Toggle activity subscription | `aniLink.anilist.mutation.toggleActivitySubscription({'id': 1})`                             |
| [saveActivityReply](AniLink/AniList/Mutations/saveActivityReply.md)                   | Save an activity reply       | `aniLink.anilist.mutation.saveActivityReply({'activityId': 1, 'text': 'Hello'})`             |
| [deleteActivityReply](AniLink/AniList/Mutations/deleteActivityReply.md)               | Delete an activity reply     | `aniLink.anilist.mutation.deleteActivityReply({'id': 1})`                                    |
| [toggleLike](AniLink/AniList/Mutations/toggleLike.md)                                 | Toggle like                  | `aniLink.anilist.mutation.toggleLike({'id': 1})`                                             |
| [toggleLikeV2](AniLink/AniList/Mutations/toggleLikeV2.md)                             | Toggle like v2               | `aniLink.anilist.mutation.toggleLikeV2({'id': 1})`                                           |
| [toggleFollow](AniLink/AniList/Mutations/toggleFollow.md)                             | Toggle follow                | `aniLink.anilist.mutation.toggleFollow({'id': 1})`                                           |
| [toggleFavourite](AniLink/AniList/Mutations/toggleFavourite.md)                       | Toggle favourite             | `aniLink.anilist.mutation.toggleFavourite({'id': 1})`                                        |
| [updateFavouriteOrder](AniLink/AniList/Mutations/updateFavouriteOrder.md)             | Update favourite order       | `aniLink.anilist.mutation.updateFavouriteOrder({'ids': [1, 2, 3]})`                          |
| [saveReview](AniLink/AniList/Mutations/saveReview.md)                                 | Save a review                | `aniLink.anilist.mutation.saveReview({'mediaId': 1, 'body': 'Review text'})`                 |
| [deleteReview](AniLink/AniList/Mutations/deleteReview.md)                             | Delete a review              | `aniLink.anilist.mutation.deleteReview({'id': 1})`                                           |
| [saveRecommendation](AniLink/AniList/Mutations/saveRecommendation.md)                 | Save a recommendation        | `aniLink.anilist.mutation.saveRecommendation({'mediaId': 1, 'body': 'Recommendation text'})` |
| [saveThread](AniLink/AniList/Mutations/saveThread.md)                                 | Save a thread                | `aniLink.anilist.mutation.saveThread({'title': 'Thread title', 'body': 'Thread body'})`      |
| [deleteThread](AniLink/AniList/Mutations/deleteThread.md)                             | Delete a thread              | `aniLink.anilist.mutation.deleteThread({'id': 1})`                                           |
| [toggleThreadSubscription](AniLink/AniList/Mutations/toggleThreadSubscription.md)     | Toggle thread subscription   | `aniLink.anilist.mutation.toggleThreadSubscription({'id': 1})`                               |
| [saveThreadComment](AniLink/AniList/Mutations/saveThreadComment.md)                   | Save a thread comment        | `aniLink.anilist.mutation.saveThreadComment({'threadId': 1, 'body': 'Comment body'})`        |
| [deleteThreadComment](AniLink/AniList/Mutations/deleteThreadComment.md)               | Delete a thread comment      | `aniLink.anilist.mutation.deleteThreadComment({'id': 1})`                                    |
| [updateAniChartSettings](AniLink/AniList/Mutations/updateAniChartSettings.md)         | Update AniChart settings     | `aniLink.anilist.mutation.updateAniChartSettings({'settings': 'Settings'})`                  |
| [updateAniChartHighlights](AniLink/AniList/Mutations/updateAniChartHighlights.md)     | Update AniChart highlights   | `aniLink.anilist.mutation.updateAniChartHighlights({'highlights': 'Highlights'})`            |