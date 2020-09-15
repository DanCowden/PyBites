"""
Function copies the given items data structure.

The tests fail. Can you fix it?

This can be done in a one liner.
"""

from copy import deepcopy

items = [{'id': 1, 'name': 'laptop', 'value': 1000},
         {'id': 2, 'name': 'chair', 'value': 300},
         {'id': 3, 'name': 'book', 'value': 20}]


def duplicate_items(items):
    items = deepcopy(items)
    return items[:]


if __name__ == '__main__':

    test = duplicate_items(items)
    print(test)
