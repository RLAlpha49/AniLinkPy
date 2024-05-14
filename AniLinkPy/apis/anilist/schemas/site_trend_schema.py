SITETRENDSCHEMA = """
  date
  count
  change
"""

"""
This is the SiteTrendSchema for the AniList API. It defines the structure of the site trend data that is expected
to be returned from the API.

Attributes:
    date (int): The date of the site trend.
    count (int): The count of the site trend.
    change (int): The change of the site trend.
"""

SITETRENDCONNECTIONSCHEMA = f"""
  pageInfo {{
    total
    perPage
    currentPage
    lastPage
    hasNextPage
  }}
  edges {{
    node {{
      {SITETRENDSCHEMA}
    }}
  }}
  nodes {{
    {SITETRENDSCHEMA}
  }}
"""

"""
This is the SiteTrendConnectionSchema for the AniList API. It defines the structure of the site trend connection
data that is expected to be returned from the API.

Attributes:
    pageInfo (dict): The page information.
    edges (dict): The edges of the site trend connection.
    nodes (dict): The nodes of the site trend connection.
"""
