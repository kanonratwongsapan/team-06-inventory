# src/inventory_no_context.py
class InventorySystem:
    def __init__(self):
        self.stock = {}
        
    def add_product(self, name, qty, price, category, threshold=15):
        self.stock[name] = {"qty": qty, "price": price, "category": category, "threshold": threshold}
        
    def issue_product(self, name, qty):
        if self.stock[name]["qty"] >= qty:
            self.stock[name]["qty"] -= qty
            if self.stock[name]["qty"] < self.stock[name]["threshold"]:
                print(f"[Email] Manager: {name} stock is low!")
                print(f"[SMS] 0812345678: {name} stock is low!")
        else:
            print("Stock not enough")