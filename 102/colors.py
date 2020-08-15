VALID_COLORS = ['blue', 'yellow', 'red']


def print_colors():
    while True:
        color = input('Enter a color: ')
        color = color.lower()

        if color == 'quit':
            print('bye')
            break
        elif color in VALID_COLORS:
            print(color)
            continue
        else:
            print('Not a valid color')
            continue
        
        pass
