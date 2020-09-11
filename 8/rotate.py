def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.

       If n is positive move characters from beginning to end
       e.g.: rotate('hello', 2) would return llohe
       if n is negative move characters to the start of the string
       e.g.: rotate('hello', -2) would return lohel
    """

    first = string[n : ]
    second = string[0 : n]
    string = first + second

    return string

    # Can shorten the above function into
    # return string[n:] + string[:n]


if __name__ == '__main__':
    string = 'hello'
    n = -2

    test = rotate(string, n)
    print(test)
