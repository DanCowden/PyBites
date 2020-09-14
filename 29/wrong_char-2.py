"""
Determine index of characters that differs from the others in respect to
being alphanumeric or not.

alphanumeric == abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789

Examples:
['A', 'f', '.', 'Q', 2]  # returns index 2 (dot differs as non-alphanumeric)
['.', '{', ' ^', '%', 'a']  # returns index 4 ('a' differs as alphanumeric)

Input:  chars list
Output:  zero-based int index
"""

import string

# Create a list of alphanumeric characters
alphanumeric_chars = list(string.ascii_letters + string.digits)

def get_index_different_char(chars):

    """ Create 2 new lists, 1 to hold the index of matched alphanumeric characters
        and 1 for non-alphanumeric
    """
    matches, no_matches = [], []

    """ Loop through List, storing index of last match for each category of
        both alphanumeric and non-alphanumeric characters """
    for index, char in enumerate(chars):
        if str(char) in alphanumeric_chars:
            matches.append(index)
        else:
            no_matches.append(index)
    # If matches List only has 1 entry (len 0) return it, otherwise return no_matches
    return matches[0] if len(matches) == 1 else no_matches[0]


if __name__ == '__main__':

    # chars = ['A', 'f', '.', 'Q', 2]
    chars = ['.', '{', ' ^', '%', 'a']

    test = get_index_different_char(chars)
    print(test)
