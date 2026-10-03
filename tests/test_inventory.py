from inventory import Inventory


# 1. สินค้าทุกรายการมีจำนวนมากกว่า threshold -> คืน list ว่าง
def test_low_stock_all_above_threshold():
    inv = Inventory()
    inv.add_stock("Apple", 10)
    inv.add_stock("Banana", 20)
    assert inv.low_stock_items(5) == []


# 2. มีสินค้าที่จำนวนเท่ากับ threshold พอดี -> ต้องถูกนับรวมด้วย
def test_low_stock_equal_to_threshold():
    inv = Inventory()
    inv.add_stock("Apple", 5)
    inv.add_stock("Banana", 10)
    assert inv.low_stock_items(5) == ["Apple"]


# 3. มีสินค้าเข้าเกณฑ์หลายรายการ -> ผลลัพธ์เรียงตามชื่อ
def test_low_stock_multiple_items_sorted_by_name():
    inv = Inventory()
    inv.add_stock("Zebra Pen", 2)
    inv.add_stock("Apple", 3)
    inv.add_stock("Mango", 10)
    inv.add_stock("Book", 1)
    assert inv.low_stock_items(5) == ["Apple", "Book", "Zebra Pen"]


# 4. คลังว่าง -> คืน list ว่าง ไม่ใช่ error
def test_low_stock_empty_inventory():
    inv = Inventory()
    assert inv.low_stock_items(5) == []


# 5. threshold เป็น 0 -> คืนเฉพาะสินค้าที่เหลือ 0
def test_low_stock_zero_threshold():
    inv = Inventory()
    inv.add_stock("Apple", 0)
    inv.add_stock("Banana", 2)
    assert inv.low_stock_items(0) == ["Apple"]


# 6. threshold ติดลบ -> คืน list ว่าง
def test_low_stock_negative_threshold():
    inv = Inventory()
    inv.add_stock("Apple", 0)
    inv.add_stock("Banana", 5)
    assert inv.low_stock_items(-1) == []