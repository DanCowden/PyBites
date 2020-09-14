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


def get_index_different_char(chars):

    # Count how many Elements contain only alphanumeric characters
    alphanum = 0
    for char in chars:
        if str(char).isalnum():
            alphanum += 1

    # Single alphanumeric entry
    if alphanum == 1:
        for index, char in enumerate(chars):
            if str(char).isalnum():
                return index
    # Single non-alphanumeric entry
    else:
        for index, char in enumerate(chars):
            if not str(char).isalnum():
                return index


if __name__ == '__main__':

    chars = ['A', 'f', '.', 'Q', 2]
    # chars = ['.', '{', ' ^', '%', 'a']

    test = get_index_different_char(chars)
    print(test)
