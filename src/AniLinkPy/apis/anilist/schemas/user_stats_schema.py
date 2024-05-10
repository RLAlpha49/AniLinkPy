"""
This is the UserAnimeStatsSchema for the Anilist API. It defines the structure of the user's anime statistics data
that is expected to be returned from the API.

Attributes:
    count (int): The count of anime the user has watched.
    meanScore (float): The mean score of the anime the user has watched.
    minutesWatched (int): The total minutes the user has watched anime.
    mediaIds (list): The list of IDs of the anime the user has watched.
"""

UserAnimeStatsSchema = """
count
meanScore
minutesWatched
mediaIds
"""

"""
This is the UserMangaStatsSchema for the Anilist API. It defines the structure of the user's manga statistics data
that is expected to be returned from the API.

Attributes:
    count (int): The count of manga the user has read.
    meanScore (float): The mean score of the manga the user has read.
    chaptersRead (int): The total chapters the user has read in manga.
    mediaIds (list): The list of IDs of the manga the user has read.
"""
UserMangaStatsSchema = """
count
meanScore
chaptersRead
mediaIds
"""
