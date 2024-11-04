"""Module for sorting songs"""
from typing import Callable


def song_length(x: tuple[str, str]) -> float:
    '''Returns the length of the song as a float,
    used for sorting by song length.

    Parameters:
    song (tuple[str, str]): A tuple containing the song title
    and its length as a string.

    Returns:
    float: The length of the song converted to a float.

    >>> song_length(('Янанебібув', '3.19'))
    3.19
    '''
    return float(x[1])



def title_length(x: tuple[str]) -> int:
    '''Returns the length of the song title,
    used for sorting by title length.

    Parameters:
    song (tuple[str, str]): A tuple containing the song title
    and its length.

    Returns:
    int: The length of the song title.

    >>> title_length(('Сосни', '4.31'))
    5
    '''
    return int(len(x[0]))


def last_word(x: tuple[str]) -> str:
    """
    Returns the first letter of the last word of the song title,
    used for sorting by last word.

    Parameters:
    song (tuple[str, str]): A tuple containing the song title and its length.

    Returns:
    str: The first letter of the last word in the song title.

    >>> last_word(('Той день', '3.58'))
    'д'
    """
    arr = x[0].split(" ")
    return arr[-1][0]


def sort_songs(
        song_titles: list[str],
        length_songs: list[str],
        key: Callable[[tuple], int | str | float]) -> list[tuple] | None:
    '''Sorts songs based on the specified key.

    Parameters:
    song_titles (list[str]): A list of song titles.
    length_songs (list[str]): A corresponding list of song lengths.
    key (Callable): The key by which to sort (song_length, title_length, last_word).

    Returns:
    list[tuple[str, str]]]: A sorted list of tuples (song title, song length)
    or None if input is invalid.

    >>> sort_songs(['Янанебібув', 'Той день', 'Мало мені', 'Сосни'],\
                   ['3.19', '3.58', '5.06', '4.31'],  song_length)
    [('Янанебібув', '3.19'), ('Той день', '3.58'), ('Сосни', '4.31'), ('Мало мені', '5.06')]
    '''
    if len(song_titles) != len(length_songs):
        return None
    arr = [(el, length_songs[i]) for i, el in enumerate(song_titles)]
    arr = sorted(arr, key = key)
    return arr

if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
