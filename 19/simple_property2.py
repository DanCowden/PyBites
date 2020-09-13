from datetime import datetime

NOW = datetime.now()


class Promo:

    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        return self.expires < NOW


if __name__ == '__main__':

    bread1 = Promo('bread', datetime(year=2016, month=12, day=19))
    print(bread1.expired)

    bread2 = Promo('bread', datetime(year=2021, month=12, day=19))
    print(bread2.expired)
