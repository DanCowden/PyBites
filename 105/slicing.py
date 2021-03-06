from string import ascii_lowercase

text = """
One really nice feature of Python is polymorphism: using the same operation
on different types of objects.
Let's talk about an elegant feature: slicing.
You can use this on a string as well as a list for example
'pybites'[0:2] gives 'py'.
 The first value is inclusive and the last one is exclusive so
here we grab indexes 0 and 1, the letter p and y.
  When you have a 0 index you can leave it out so can write this as 'pybites'[:2]
but here is the kicker: you can use this on a list too!
['pybites', 'teaches', 'you', 'Python'][-2:] would gives ['you', 'Python']
and now you know about slicing from the end as well :)
keep enjoying our bites!
"""


def slice_and_dice(text: str = text) -> list:
    """Get a list of words from the passed in text.
       See the Bite description for step by step instructions"""

    results = []

    # Strip off both leading and trailing whitespace
    # Split string by \n
    for line in text.strip().splitlines():
        # Strip off any leading spaces
        line = line.lstrip()
        # Check if the first character in string is lowercase
        if line[0] in ascii_lowercase:
            # Split line into words
            words = line.split()
            # Get the last word
            # strip off trailing . and ! characters
            last_word = words[-1].rstrip('.!')

            # Add last word to the results list
            results.append(last_word)

    return results
