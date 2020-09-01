def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""

    try:
        numerator = int(numerator)
    except ValueError:
        raise ValueError(f'Could not convert numerator {numerator} '
                        f'into an integer')

    try:
        denominator = int(denominator)
    except ValueError:
        raise ValueError(f'Could not convert denominator {denominator} '
                        f'into an integer')

    try:
        answer = (numerator / denominator)
    except ZeroDivisionError:
        return 0
    else:
        return answer


if __name__ == '__main__':
    numerator = 8
    denominator = 2

    x = divide_numbers(numerator, denominator)
    print(x)
