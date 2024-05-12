# AniLinkPy

AniLink is a Python library for interacting with the AniList API. It provides methods for querying and mutating data, making it easier to integrate AniList's features into your own applications.

## Installation

Installing AniLinkPy is straightforward. The recommended approach is to use a project manager like Poetry or Hatch, as these tools provide a clean, isolated environment for your project. Alternatively, you can use pipx, which automatically sandboxes your pip installations into separate environments. If you prefer to use pip, you can install AniLinkPy directly as well.

=== "Poetry"

    In `pyproject.toml`:
    
    ```bash
    [tool.poetry.dependencies]
    AniLinkPy = "*" # (1)!
    ```

    1.  The `*` will install the latest version of AniLinkPy. You can also specify a version number to install a specific version. 

        !!! example "Specifying a Version"
            ```bash
            [tool.poetry.dependencies]
            AniLinkPy = "1.0.0"
            ```

=== "Hatch"

    In `pyproject.toml`:
    
    ```bash
    dependencies = [
        "AniLinkPy" # (1)!
    ]
    ```

    1.  To install a specific version of AniLinkPy, you can specify the version number in the dependencies list:
    
        !!! example "Specifying a Version"
            ```bash
            dependencies = [
                "AniLinkPy==1.0.0"
            ]
            ```

=== "pipx"

    Run the following command in your terminal:    

    ```bash
    pipx install AniLinkPy # (1)!
    ```
    
    1.  To install a specific version of AniLinkPy, you can specify the version number with the package name:
        
        !!! example "Specifying a Version"
            ```bash
            pipx install AniLinkPy==1.0.0
            ```

=== "Pip"

    Run the following command in your terminal:    

    ```bash
    pip install AniLinkPy # (1)!
    ```
    
    1.  To install a specific version of AniLinkPy:
    
        !!! example "Specifying a Version"
            ```bash
            pip install AniLinkPy==1.0.0
            ```

## Initialization

### AniList

To start using AniLink, you need to import it and initialize it with an optional authentication token. You can get an authentication token by registering your application on the AniList website.

!!! example "Importing & Initializing AniLink"

    ```python
    from AniLinkPy import AniLink

    auth_token = 'your-auth-token' # (1)!
    aniLink = AniLink(auth_token)
    ```

    1.  Please replace `'your-auth-token'` with your actual authentication token.

    You can also initialize AniLink without an authentication token
    
    ```python
    aniLink = AniLink()
    ```

## AniList API

### Structure

AniLink for AniList is divided into two main sections: `anilist.query` and `anilist.mutation`. The `anilist.query` section contains methods for querying data from the AniList API, while the `anilist.mutation` section contains methods for mutating data.

#### Custom Queries and Mutations

If needed there is a custom section `anilist.custom` that allows the user to pass a custom query or mutation to the AniList API.

The method accepts two parameters: the query or mutation string and an optional variables object.

!!! example "Custom Query"

    ```python
    viewer = aniLink.anilist.custom('query {Viewer {id}}')
    
    mutation = 'mutation ($about: String) {UpdateUser (about: $about) {id}}'
    variables = { 'about': "New about text" }
    response = aniLink.anilist.custom(mutation, variables)
    ```

#### Query Methods

The `anilist.query` section is further divided into main query methods and page query methods. The main query methods return a single piece of data, while the page query methods return pages of data.

List of main query methods in `anilist.query`:

- [x] [user](AniLink/AniList/Queries/user.md)
- [ ] [media](AniLink/AniList/Queries/media.md)
- [ ] [mediaTrend](AniLink/AniList/Queries/mediaTrend.md)
- [ ] [airingSchedule](AniLink/AniList/Queries/airingSchedule.md)
- [ ] [character](AniLink/AniList/Queries/character.md)
- [ ] [staff](AniLink/AniList/Queries/staff.md)
- [ ] [mediaList](AniLink/AniList/Queries/mediaList.md)
- [ ] [mediaListCollection](AniLink/AniList/Queries/mediaListCollection.md)
- [ ] [genreCollection](AniLink/AniList/Queries/genreCollection.md)
- [ ] [mediaTagCollection](AniLink/AniList/Queries/mediaTagCollection.md)
- [ ] [viewer](AniLink/AniList/Queries/viewer.md)
- [ ] [notification](AniLink/AniList/Queries/notification.md)
- [ ] [studio](AniLink/AniList/Queries/studio.md)
- [ ] [review](AniLink/AniList/Queries/review.md)
- [ ] [activity](AniLink/AniList/Queries/activity.md)
- [ ] [activityReply](AniLink/AniList/Queries/activityReply.md)
- [ ] [following](AniLink/AniList/Queries/following.md)
- [ ] [follower](AniLink/AniList/Queries/follower.md)
- [ ] [thread](AniLink/AniList/Queries/thread.md)
- [ ] [threadComment](AniLink/AniList/Queries/threadComment.md)
- [ ] [recommendation](AniLink/AniList/Queries/recommendation.md)
- [ ] [markdown](AniLink/AniList/Queries/markdown.md)
- [ ] [aniChartUser](AniLink/AniList/Queries/aniChartUser.md)
- [ ] [siteStatistics](AniLink/AniList/Queries/siteStatistics.md)
- [ ] [externalLinkSourceCollection](AniLink/AniList/Queries/externalLinkSourceCollection.md)

List of page query methods in `anilist.query.page`:

- [ ] [users](AniLink/AniList/Queries/Page/users.md)
- [ ] [medias](AniLink/AniList/Queries/Page/medias.md)
- [ ] [characters](AniLink/AniList/Queries/Page/characters.md)
- [ ] [staffs](AniLink/AniList/Queries/Page/staffs.md)
- [ ] [studios](AniLink/AniList/Queries/Page/studios.md)
- [ ] [mediaLists](AniLink/AniList/Queries/Page/mediaLists.md)
- [ ] [airingSchedules](AniLink/AniList/Queries/Page/airingSchedules.md)
- [ ] [mediaTrends](AniLink/AniList/Queries/Page/mediaTrends.md)
- [ ] [notifications](AniLink/AniList/Queries/Page/notifications.md)
- [ ] [followers](AniLink/AniList/Queries/Page/followers.md)
- [ ] [following](AniLink/AniList/Queries/Page/following.md)
- [ ] [activities](AniLink/AniList/Queries/Page/activities.md)
- [ ] [activityReplies](AniLink/AniList/Queries/Page/activityReplies.md)
- [ ] [threads](AniLink/AniList/Queries/Page/threads.md)
- [ ] [threadComments](AniLink/AniList/Queries/Page/threadComments.md)
- [ ] [reviews](AniLink/AniList/Queries/Page/reviews.md)
- [ ] [recommendations](AniLink/AniList/Queries/Page/recommendations.md)
- [ ] [likes](AniLink/AniList/Queries/Page/likes.md)

#### Mutation Methods

List of methods in `anilist.mutation`:

- [ ] [updateUser](AniLink/AniList/Mutations/updateUser.md)
- [ ] [saveMediaListEntry](AniLink/AniList/Mutations/saveMediaListEntry.md)
- [ ] [updateMediaListEntries](AniLink/AniList/Mutations/updateMediaListEntries.md)
- [ ] [deleteMediaListEntries](AniLink/AniList/Mutations/deleteMediaListEntries.md)
- [ ] [deleteCustomLists](AniLink/AniList/Mutations/deleteCustomLists.md)
- [ ] [saveTextActivity](AniLink/AniList/Mutations/saveTextActivity.md)
- [ ] [saveMessageActivity](AniLink/AniList/Mutations/saveMessageActivity.md)
- [ ] [deleteActivity](AniLink/AniList/Mutations/deleteActivity.md)
- [ ] [toggleActivityPin](AniLink/AniList/Mutations/toggleActivityPin.md)
- [ ] [toggleActivitySubscription](AniLink/AniList/Mutations/toggleActivitySubscription.md)
- [ ] [saveActivityReply](AniLink/AniList/Mutations/saveActivityReply.md)
- [ ] [deleteActivityReply](AniLink/AniList/Mutations/deleteActivityReply.md)
- [ ] [toggleLike](AniLink/AniList/Mutations/toggleLike.md)
- [ ] [toggleLikeV2](AniLink/AniList/Mutations/toggleLikeV2.md)
- [ ] [toggleFollow](AniLink/AniList/Mutations/toggleFollow.md)
- [ ] [toggleFavourite](AniLink/AniList/Mutations/toggleFavourite.md)
- [ ] [updateFavouriteOrder](AniLink/AniList/Mutations/updateFavouriteOrder.md)
- [ ] [saveReview](AniLink/AniList/Mutations/saveReview.md)
- [ ] [deleteReview](AniLink/AniList/Mutations/deleteReview.md)
- [ ] [saveRecommendation](AniLink/AniList/Mutations/saveRecommendation.md)
- [ ] [saveThread](AniLink/AniList/Mutations/saveThread.md)
- [ ] [deleteThread](AniLink/AniList/Mutations/deleteThread.md)
- [ ] [toggleThreadSubscription](AniLink/AniList/Mutations/toggleThreadSubscription.md)
- [ ] [saveThreadComment](AniLink/AniList/Mutations/saveThreadComment.md)
- [ ] [deleteThreadComment](AniLink/AniList/Mutations/deleteThreadComment.md)
- [ ] [updateAniChartSettings](AniLink/AniList/Mutations/updateAniChartSettings.md)
- [ ] [updateAniChartHighlights](AniLink/AniList/Mutations/updateAniChartHighlights.md)

### Error Handling

AniLink will throw an error if the AniList API returns an error. You can catch these errors using a try-except block.

!!! example "Error Handling"

    ```python
    try:
      user = aniLink.anilist.query.user({'id': 542244})
      print(user)
    except Exception as error:
      print(error)
    ```

This includes status codes and error messages returned by the AniList API. Here is an example rate limit handler to catch the errors thrown by AniLink:

```python
import time

async def handle_rate_limit(api_call, retry_after=60):
    while True:
        try:
            response = await api_call()
            print(response)
            return response
        except Exception as error:
            if '429' in str(error):
                print('Rate limit exceeded, waiting for 1 minute before retrying...')
                time.sleep(retry_after)
                print('Retrying...')
            else:
                raise error
```

???+ note "Error Codes"

    The possible error codes returned by the AniList API are:
    
    - 400: Bad Request (e.g. missing variables, invalid variables, or invalid query)
    - 401: Unauthorized (e.g. invalid authentication token)
    - 404: Not Found (e.g. user not found)
    - 429: Too Many Requests (e.g. rate limit exceeded)
    - 500: Internal Server Error (e.g. AniList server error)

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/RLAlpha49/AniLinkPy/blob/master/LICENSE) file for details.