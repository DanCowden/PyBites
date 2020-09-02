NAMES = ['arnold schwarzenegger', 'alec baldwin', 'bob belderbos',
         'julian sequeira', 'sandra bullock', 'keanu reeves',
         'julbob pybites', 'bob belderbos', 'julian sequeira',
         'al pacino', 'brad pitt', 'matt damon', 'brad pitt']


def dedup_and_title_case_names(names):
    """Should return a list of title cased names,
       each name appears only once"""

    unique_list = []

    for name in names:
        if name.title() not in unique_list:
            unique_list.append(name.title())

    return unique_list


def sort_by_surname_desc(names):
    """Returns names list sorted desc by surname"""

    names = dedup_and_title_case_names(names)
    return sorted(names, key=lambda x: x.split(" ")[-1], reverse=True)


def shortest_first_name(names):
    """Returns the shortest first name (str).
       You can assume there is only one shortest name.
    """
    names = dedup_and_title_case_names(names)

    shortest = ""

    for name in names:
        if len(shortest) == 0:
            shortest = name.split(" ")[0]
        elif len(name.split(" ")[0]) < len(shortest):
            shortest = name.split(" ")[0]

    return shortest


if __name__ == '__main__':
    unique_names = dedup_and_title_case_names(NAMES)
    print(unique_names)

    sorted_names = sort_by_surname_desc(NAMES)
    print(sorted_names)

    shortest_name = shortest_first_name(NAMES)
    print(shortest_name)
