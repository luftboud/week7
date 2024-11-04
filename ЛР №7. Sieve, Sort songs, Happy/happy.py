"""Module for operations with happy numbers"""
def happy_number(number: int) -> bool:
    """
    Determines if a ticket number is a happy number.

    Parameters:
    num (int): The ticket number to check.

    Returns:
    bool: True if the ticket is a happy number, False otherwise.

    >>> happy_number(1234)
    False
    >>> happy_number(32100123)
    True
    >>> happy_number(159123)
    True
    """
    number = str(number)
    if len(number)<8:
        zero_q = 8 - len(number)
        number = zero_q * "0" + number
    arr = [int(el) for el in number]
    # print(arr[4:])
    arr1 = arr[:4]
    arr2 = arr[4:]
    while True:
        sum1 = str(sum(arr1))
        arr1 = [int(el) for el in sum1]

        if len(arr1) == 1:
            break
    while True:
        sum2 = str(sum(arr2))
        arr2 = [int(el) for el in sum2]
        if len(arr2) == 1:
            break
    if arr1[0] == arr2[0]:
        return True
    return False


def count_happy_numbers(n: int) -> int:
    """
    Counts the number of happy tickets from 1 to n inclusive.

    Parameters:
    n (int): The upper limit of ticket numbers to check.

    Returns:
    int: The count of happy tickets in the range.

    >>> count_happy_numbers(10001)
    1
    >>> count_happy_numbers(10010)
    2
    >>> count_happy_numbers(10100)
    12
    >>> count_happy_numbers(100000)
    9999
    """
    counter = 0
    arr = list(range(1, n+1))
    for el in arr:
        if happy_number(el):
            counter += 1
    return counter


def happy_numbers(m: int, n: int) -> list[int]:
    """
    Generates a list of happy ticket numbers within the given range.

    Parameters:
    m (int): The lower limit of ticket numbers (inclusive).
    n (int): The upper limit of ticket numbers (inclusive).

    Returns:
    list[int]: A list of happy ticket numbers in the range.

    >>> happy_numbers(1, 10001)
    [10001]
    >>> happy_numbers(10001, 10010)
    [10001, 10010]
    >>> happy_numbers(1, 11)
    []
    >>> happy_numbers(10001, 10100)
    [10001, 10010, 10019, 10028, 10037, 10046, 10055, 10064, 10073, 10082, 10091, 10100]
    """
    happy = []
    arr = list(range(m, n+1))
    for el in arr:
        if happy_number(el):
            happy.append(el)
    return happy



if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
