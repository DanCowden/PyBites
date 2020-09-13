"""
Write a simple Promo class. Its constructor receives two variables:
name (which must be a string) and expires (which must be a datetime object)

Add a property called expired which returns a boolean value indicating whether
the promo has expired or not.
"""

from datetime import datetime

NOW = datetime.now()


class Promo:

    def __init__(self, name, expires):
        self.name = name
        self.expires = expires

    @property
    def expired(self):
        if self.expires < NOW:
            return True
        else:
            return False


if __name__ == '__main__':

    bread1 = Promo('bread', datetime(year=2016, month=12, day=19))
    print(bread1.expired)

    bread2 = Promo('bread', datetime(year=2021, month=12, day=19))
    print(bread2.expired)
