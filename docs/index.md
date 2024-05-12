# AniLinkPy

AniLink is a Python library for interacting with the AniList API. It provides methods for querying and mutating data, making it easier to integrate AniList's features into your own applications.

<div class="grid cards" markdown>

-   :material-download:{ .lg .middle } __Install__

    ---

    Install AniLink with `poetry`, `hatch`, `pip` or `pipx` and start using it in minutes

    [:octicons-arrow-right-24: Installation](installation)

</div>

<div class="grid cards" markdown>

-   :simple-anilist:{ .lg .middle } __AniList__

    ---

    Use AniLink to query and mutate data from the AniList API

    [:octicons-arrow-right-24: AniList API](AniListAPI)

-   :simple-myanimelist:{ .lg .middle } __MyAnimeList__

    ---

    Coming soon: Use AniLink to query and mutate data from the MyAnimeList API

    [:octicons-arrow-right-24: MyAnimeList API](MyAnimeListAPI)

-   :simple-kitsu:{ .lg .middle } __Kitsu__

    ---

    Coming soon: Use AniLink to query and mutate data from the Kitsu API

    [:octicons-arrow-right-24: Kitsu API](KitsuAPI)

</div>

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

This includes status codes and error messages returned by the APIs. Here is an example rate limit handler to catch the errors thrown by AniLink:

```python
def handle_rate_limit(api_call, retry_after=60):
    while True:
        try:
            response = api_call()
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

=== "AniList"
    ???+ note "Error Codes"
        
        The possible error codes returned by the AniList API are:

        | Status Code | Description           | Example                                                |
        |-------------|-----------------------| ------------------------------------------------------ |
        | 400         | Bad Request           | Missing variables, invalid variables, or invalid query |
        | 401         | Unauthorized          | Invalid authentication token                           |
        | 404         | Not Found             | User not found                                         |
        | 429         | Too Many Requests     | Rate limit exceeded                                    |
        | 500         | Internal Server Error | AniList server                                         |

## License

This project is licensed under the MIT License - see the [LICENSE](https://github.com/RLAlpha49/AniLinkPy/blob/master/LICENSE) file for details.