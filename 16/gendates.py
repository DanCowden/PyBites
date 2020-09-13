from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    date = PYBITES_BORN
    birthday = PYBITES_BORN
    days = 0
    while True:
        date += timedelta(days=100)
        days += 100
        if days == 400:
            birthday = birthday.replace(year=birthday.year + 1)
            yield birthday
        elif days == 800:
            birthday = birthday.replace(year=birthday.year + 1)
            yield birthday
        yield date


if __name__ == '__main__':
    hundred_days = gen_special_pybites_dates()

    for x in range(10):
        print(next(hundred_days))
