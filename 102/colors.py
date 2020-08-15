VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    while True:
        color = input('Enter a color: ').lower()

        if color == 'quit':
            print('bye')
            break

        if color not in VALID_COLORS:
            print('Not a valid color')
            continue
        
        print(color)

        pass
