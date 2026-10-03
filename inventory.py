class Inventory:
    def __init__(self):
        self.items = {}

    def add_stock(self, name: str, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self.items[name] = self.items.get(name, 0) + quantity

    def sell(self, name: str, quantity: int):
        if name not in self.items:
            raise KeyError(f"Item '{name}' not found in inventory")
        if not isinstance(quantity, int) or isinstance(quantity, bool):
            raise TypeError("Quantity must be an integer")
        if quantity <= 0:
            raise ValueError("Quantity to sell must be greater than zero")
        if self.items[name] < quantity:
            raise ValueError("Insufficient stock")
        self.items[name] -= quantity
        return self.items[name]

    def low_stock_items(self, threshold: int) -> list[str]:
        if threshold < 0:
            return []
        low_stock_names = [
            item_name
            for item_name, quantity in self.items.items()
            if quantity <= threshold
        ]
        return sorted(low_stock_names)
