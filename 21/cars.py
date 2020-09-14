import re

cars = {
    'Ford': ['Falcon', 'Focus', 'Festiva', 'Fairlane'],
    'Holden': ['Commodore', 'Captiva', 'Barina', 'Trailblazer'],
    'Nissan': ['Maxima', 'Pulsar', '350Z', 'Navara'],
    'Honda': ['Civic', 'Accord', 'Odyssey', 'Jazz'],
    'Jeep': ['Grand Cherokee', 'Cherokee', 'Trailhawk', 'Trackhawk']
}


def get_all_jeeps(cars=cars):
    """return a comma  + space (', ') separated string of jeep models
       (original order)"""
    # Converting List to a single string
    return ', '.join(cars['Jeep'])


def get_first_model_each_manufacturer(cars=cars):
    """
    return a list of the first car in each dict value list (original ordering)
    """
    first_car = []
    for value in cars.values():
        first_car.append(value[0])
    return first_car


def get_all_matching_models(cars=cars, grep='trail'):
    """return a list of all models containing the case insensitive
       'grep' string which defaults to 'trail' for this exercise,
       sort the resulting sequence alphabetically"""
    matches = []
    p = re.compile(grep, re.I)
    for value in cars.values():
        for car in value:
            if p.search(car):
                matches.append(car)
    return sorted(matches)


def sort_car_models(cars=cars):
    """return a copy of the cars dict with the car models (values)
       sorted alphabetically"""
    new_dict = {}
    for k, v in cars.items():
        value = sorted(v)
        new_dict[k] = value
    return new_dict


if __name__ == '__main__':

    all_jeeps = get_all_jeeps()
    print('Test #1')
    print(all_jeeps)

    first_car = get_first_model_each_manufacturer()
    print('Test #2')
    print(first_car)

    find_car = get_all_matching_models()
    print('Test #3')
    print(find_car)

    car_models = sort_car_models()
    print('Test #4')
    print(car_models)
