class Item:
    def __init__(self, id, name, category, price):
        self._id = id
        self._name = name
        self._category = category
        self._price = price

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @property
    def category(self):
        return self._category

    @property
    def price(self):
        return self._price

    def __repr__(self):
        return f"Item ({self.id}, {self.category}, {self.price})"


class Cart:
    def __init__(self):
        self._items = dict()

    def set_item_qty(self, item, quantity):
        # to encapsulate behavior of trying to add the same item multiple times
        # This can be seen as either an idempotent operation (current implementation) or
        # programming error (in this case it would've raised an exception)
        self._items[item.id] = (item, quantity)

    def add_items(self, item_list):
        for item, quantity in item_list:
            self.set_item_qty(item, quantity)

    @property
    def items(self):
        return self._items.values()

    def get_item_quantity(self, item):
        item, qty = self._items[item.id]
        return qty

    def __repr__(self):
        return f"Cart {list(self.items)}"
