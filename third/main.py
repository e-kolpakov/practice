from datetime import datetime, timedelta
from decimal import Decimal

from third.customer import Customer, Affiliate, Employee
from third.cart import Cart, Item
from third.discount import DiscountCalculator

if __name__ == "__main__":
    now = datetime(2019, 1, 1)
    customer1 = Customer(join_date=datetime(2018, 12, 1))
    customer2 = Customer(join_date=datetime(2016, 12, 31))
    employee = Employee(join_date=datetime(2018, 12, 1))
    affiliate = Affiliate(join_date=datetime(2018, 12, 1))

    assert customer1.customer_discount(now) == Decimal(0)
    assert customer2.customer_discount(now) == Decimal('0.05')
    assert employee.customer_discount(now) == Decimal('0.3')
    assert affiliate.customer_discount(now) == Decimal('0.1')

    cart = Cart()
    cart.add_items([
        (Item(1, "milk", "groceries", Decimal(10)), 2),
        (Item(2, "bread", "groceries", Decimal(3.5)), 2),
        (Item(3, "TV", "electronics", Decimal(100)), 1),
        (Item(4, "electric bulb", "electronics", Decimal(2)), 5),
    ])

    customer1_pays = DiscountCalculator.calculate_net_payabable_amount(customer1, cart, now)
    # groceries sum is 27, non-groceries is 110, total 137, discount 5
    assert customer1_pays == 132, customer1_pays

    customer2_pays = DiscountCalculator.calculate_net_payabable_amount(customer2, cart, now)
    # groceries sum is 27, non-groceries is 110 * 0.95 = 104.5, total 131.5, discount 5
    assert customer2_pays == 126.5, customer2_pays

    employee_pays = DiscountCalculator.calculate_net_payabable_amount(employee, cart, now)
    # groceries sum is 27, non-groceries is 110 * 0.7 = 77, total 104, discount 5
    assert employee_pays == 99, employee_pays

    affiliate_pays = DiscountCalculator.calculate_net_payabable_amount(affiliate, cart, now)
    # groceries sum is 27, non-groceries is 110 * 0.9 = 99, total 104, discount 5
    assert affiliate_pays == 121, affiliate_pays
