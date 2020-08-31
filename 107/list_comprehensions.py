def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""

    positive_even_numbers = [x for x in numbers if x > 0 and not x % 2]

    return positive_even_numbers


numbers = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
x = filter_positive_even_numbers(numbers)
print(x)

