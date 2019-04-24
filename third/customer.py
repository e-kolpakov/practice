from decimal import Decimal
from datetime import datetime
from dateutil.relativedelta import relativedelta


class AbstractCustomer:
    def __init__(self, join_date: datetime):
        # in complied statically typed language (Java, Scala, C++, Haskell, etc.) this would be enforced by the compiler
        # in interpreted language, assert on te type is the next best thing
        assert type(join_date) is datetime, f"join_date should be datetime, but was {join_date}"
        self._join_date = join_date
        self._discount = None  # lazy evaluation

    @property
    def customer_type(self):
        return self._type

    @property
    def join_date(self):
        return self._join_date

    # there are multiple ways to handle the notion of current_date_time here
    # in this case, we'll just pass it down.

    # One other viable alternative would be to extract the logic of calculating discount to a separate class
    # and than pass a "current_date_time_provider" - but such approach actually suits functional programming better
    def customer_discount(self, current_date):
        assert type(current_date) is datetime, f"current_date should be datetime, but was {current_date}"
        affiliation_discount = self._customer_affiliation_discount()
        join_date_discount = self._join_date_discount(current_date)

        return max(affiliation_discount, join_date_discount)

    def _customer_affiliation_discount(self):
        # A "lightweight" way to make the class abstract in python
        # A "proper" way is to use abstract base class package (aka abc) + ABCMeta metaclass, but in this case it's
        # more trouble than benefit
        raise NotImplementedError("Must be overridden in descendent class")

    def _join_date_discount(self, date):
        if self.join_date + relativedelta(years=2) < date:
            return Decimal('0.05')
        else:
            return Decimal('0')


class Employee(AbstractCustomer):
    def __init__(self, join_date):
        super().__init__(join_date)

    def _customer_affiliation_discount(self):
        return Decimal('0.3')


class Affiliate(AbstractCustomer):
    def __init__(self, join_date):
        super().__init__(join_date)

    def _customer_affiliation_discount(self):
        return Decimal('0.1')


class Customer(AbstractCustomer):
    def __init__(self, join_date):
        super().__init__(join_date)

    def _customer_affiliation_discount(self):
        return Decimal(0)
