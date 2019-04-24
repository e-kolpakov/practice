from datetime import datetime
from decimal import Decimal

from third.customer import AbstractCustomer
from third.cart import Cart


class DiscountCalculator:
    @classmethod
    def calculate_net_payabable_amount(cls, customer, cart, date):
        assert isinstance(customer, AbstractCustomer), f"Expected Customer, but was {customer}"
        assert isinstance(cart, Cart), f"Expected Cart, but was {cart}"
        assert isinstance(date, datetime), f"current_date should be datetime, but was {current_date}"
        customer_discount = customer.customer_discount(date)

        total_price = sum([
            cls._discounted_item_price(item, customer_discount) * quantity
            for item, quantity in cart.items
        ])
        amount_discount = cls._amount_discount(total_price)
        return total_price - amount_discount

    @staticmethod
    def _discounted_item_price(item, customer_discount):
        discount = customer_discount if item.category != "groceries" else Decimal(0)
        return item.price * (Decimal(1) - discount)

    @staticmethod
    def _amount_discount(total_price):
        return total_price // 100 * Decimal(5)
