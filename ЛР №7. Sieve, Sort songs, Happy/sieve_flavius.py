"""Module for finding lucky numbers"""
def sieve_flavius(n: int) -> list[int]:
    '''Generates a list of lucky numbers not exceeding the given number n.

    Parameters:
    n (int): The upper limit for generating lucky numbers.

    Returns:
    list[int]: A list of lucky numbers up to n.

    >>> sieve_flavius(100)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
    >>> sieve_flavius(33)
    [1, 3, 7, 9, 13, 15, 21, 25, 31, 33]
    >>> sieve_flavius(10)
    [1, 3, 7, 9]
    >>> sieve_flavius(0)
    []
    '''
    arr = list(range(1,n+1))
    for i in range(1, len(arr)//2+1):
        arr.remove(2*i)
    i = 1
    while True:
        try:
            el = arr[i]
            remove_arr = arr[el-1::el]
            arr = [num for num in arr if num not in remove_arr]
            i += 1
        except IndexError:
            return arr




if __name__ == '__main__':
    import doctest
    print(doctest.testmod())
