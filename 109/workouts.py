WORKOUT_SCHEDULE = {'Friday': 'Shoulders',
                    'Monday': 'Chest+biceps',
                    'Saturday': 'Rest',
                    'Sunday': 'Rest',
                    'Thursday': 'Legs',
                    'Tuesday': 'Back+triceps',
                    'Wednesday': 'Core'}
REST, CHILL_OUT, TRAIN = 'Rest', 'Chill out!', 'Go train {}'
INVALID_DAY = 'Not a valid day'


def get_workout_motd(day):

    # Using Title Case to format incoming day
    day = day.title()

    # If day is not in WORKOUT_SCHEDULE, return INVALID_DAY
    if day not in WORKOUT_SCHEDULE.keys():
        return INVALID_DAY

    """
    If day is in WORKOUT_SCHEDULE retrieve the value (workout)
       and return the following:
       - weekday, return TRAIN with the workout value interpolated
            Eg. Thursday -> function returns 'Go train Legs'
       - weekend day (value 'Rest'), return CHILL_OUT
    """
    for workout_day, workout in WORKOUT_SCHEDULE.items():
        if day == workout_day:
            if workout == 'Rest':
                return CHILL_OUT
            else:
                return TRAIN.format(workout)
    pass

day = 'SUNDAY'

x = get_workout_motd(day)
print(x)
