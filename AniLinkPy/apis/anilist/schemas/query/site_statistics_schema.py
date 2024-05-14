from AniLinkPy.apis.anilist.schemas.site_trend_schema import SITETRENDCONNECTIONSCHEMA

SITESTATISTICSSCHEMA = f"""
  users (sort: $usersSort, page: $usersPage, perPage: $usersPerPage) {{
    {SITETRENDCONNECTIONSCHEMA}
  }}
  anime (sort: $animeSort, page: $animePage, perPage: $animePerPage) {{
    {SITETRENDCONNECTIONSCHEMA}
  }}
  manga (sort: $mangaSort, page: $mangaPage, perPage: $mangaPerPage) {{
    {SITETRENDCONNECTIONSCHEMA}
  }}
  characters (sort: $charactersSort, page: $charactersPage, perPage: $charactersPerPage) {{
    {SITETRENDCONNECTIONSCHEMA}
  }}
  staff (sort: $staffSort, page: $staffPage, perPage: $staffPerPage) {{
    {SITETRENDCONNECTIONSCHEMA}
  }}
  studios (sort: $studiosSort, page: $studiosPage, perPage: $studiosPerPage) {{
    {SITETRENDCONNECTIONSCHEMA}
  }}
  reviews (sort: $reviewsSort, page: $reviewsPage, perPage: $reviewsPerPage) {{
    {SITETRENDCONNECTIONSCHEMA}
  }}
"""

"""
SiteStatisticsSchema is a string representing the GraphQL schema for a site statistics query.
It includes users, anime, manga, characters, staff, studios, and reviews of type `SiteTrendConnection`.

Attributes:
    users (str): The users schema of the site statistics.
    anime (str): The anime schema of the site statistics.
    manga (str): The manga schema of the site statistics.
    characters (str): The characters schema of the site statistics.
    staff (str): The staff schema of the site statistics.
    studios (str): The studios schema of the site statistics.
    reviews (str): The reviews schema of the site statistics.
"""
