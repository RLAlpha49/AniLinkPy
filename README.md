
# AniLinkPy Documentation

AniLinkPy is a Python library that provides an interface to interact with anime/manga APIs like AniList, MyAnimeList, and Kitsu. The library is structured as follows:

## Main Components

- `AniLink`: The main class that initializes connections to different APIs
- `AniList`: Class for interacting with the AniList API
  - `Query`: Methods for querying data
  - `Mutation`: Methods for mutating data
  - `CustomRequest`: For sending custom queries/mutations

## Key Features

- Query methods for retrieving data on users, media, characters, etc.
- Mutation methods for updating data 
- Page query methods for paginated results
- Custom query/mutation support
- Error handling for API errors

## Usage

Basic usage:

```python
from AniLinkPy import AniLink

anilink = AniLink(auth_token)

# Query a user
user = anilink.anilist.query.user({'id': 123})

# Custom query
custom_query = """
  query {
    Viewer {
      id
    }
  }
"""
result = anilink.anilist.custom(custom_query)
```

The library handles authentication, request sending, and response parsing. It provides a clean interface to interact with anime/manga APIs without having to deal with the low-level details.

## Installation

AniLinkPy can be installed via pip:

```
pip install AniLinkPy
```

## Error Handling

The library throws exceptions for API errors which can be caught and handled:

```python 
try:
  user = anilink.anilist.query.user({'id': 123})
except Exception as error:
  print(error)
```

Overall, AniLinkPy aims to simplify interaction with anime/manga APIs by providing an intuitive Python interface.
