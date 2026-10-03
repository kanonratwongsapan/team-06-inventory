import pytest

from inventory import Inventory


# --- ขั้นที่ 2: ชุด TDD สำหรับ low_stock_items ---
def test_low_stock_all_above_threshold():
    inv = Inventory()
    inv.add_stock("Apple", 10)
    inv.add_stock("Banana", 20)
    assert inv.low_stock_items(5) == []


def test_low_stock_equal_to_threshold():
    inv = Inventory()
    inv.add_stock("Apple", 5)
    inv.add_stock("Banana", 10)
    assert inv.low_stock_items(5) == ["Apple"]


def test_low_stock_multiple_items_sorted_by_name():
    inv = Inventory()
    inv.add_stock("Zebra Pen", 2)
    inv.add_stock("Apple", 3)
    inv.add_stock("Mango", 10)
    inv.add_stock("Book", 1)
    assert inv.low_stock_items(5) == ["Apple", "Book", "Zebra Pen"]


def test_low_stock_empty_inventory():
    inv = Inventory()
    assert inv.low_stock_items(5) == []


def test_low_stock_zero_threshold():
    inv = Inventory()
    inv.add_stock("Apple", 0)
    inv.add_stock("Banana", 2)
    assert inv.low_stock_items(0) == ["Apple"]


def test_low_stock_negative_threshold():
    inv = Inventory()
    inv.add_stock("Apple", 0)
    inv.add_stock("Banana", 5)
    assert inv.low_stock_items(-1) == []


# --- ขั้นที่ 4: Test เมธอด sell (กรณีปกติจาก AI + เขียนเสริม Edge Cases) ---
def test_sell_normal_case():
    inv = Inventory()
    inv.add_stock("Apple", 10)
    remaining = inv.sell("Apple", 4)
    assert remaining == 6


# 1. กลุ่มค่าขอบ: ขายเท่ากับจำนวนที่เหลือทั้งหมดพอดี ต้องเหลือ 0
def test_sell_exact_remaining_stock():
    inv = Inventory()
    inv.add_stock("Apple", 5)
    assert inv.sell("Apple", 5) == 0


# 2. กลุ่มค่าที่ไม่ควรรับ (1): ขายจำนวน 0 หรือติดลบ ต้องเกิด ValueError
def test_sell_zero_or_negative_quantity():
    inv = Inventory()
    inv.add_stock("Apple", 5)
    with pytest.raises(ValueError, match="greater than zero"):
        inv.sell("Apple", 0)
    with pytest.raises(ValueError, match="greater than zero"):
        inv.sell("Apple", -3)


# 3. กลุ่มค่าที่ไม่ควรรับ (2): ขายเกินจำนวนที่เหลือในคลัง ต้องเกิด ValueError
def test_sell_more_than_stock():
    inv = Inventory()
    inv.add_stock("Apple", 5)
    with pytest.raises(ValueError, match="Insufficient stock"):
        inv.sell("Apple", 6)


# 4. กลุ่มเส้นทาง error: ขายสินค้าที่ไม่มีในคลัง ต้องเกิด KeyError พร้อมข้อความ
def test_sell_non_existent_item():
    inv = Inventory()
    with pytest.raises(KeyError, match="not found in inventory"):
        inv.sell("Orange", 1)


# 5. กลุ่มชนิดข้อมูล: ใส่จำนวนเป็นทศนิยมหรือข้อความ ต้องเกิด TypeError
def test_sell_invalid_data_type():
    inv = Inventory()
    inv.add_stock("Apple", 5)
    with pytest.raises(TypeError, match="must be an integer"):
        inv.sell("Apple", 2.5)
    with pytest.raises(TypeError, match="must be an integer"):
        inv.sell("Apple", "two")


# เพิ่มเติมเพื่อความครอบคลุม: ทดสอบการเพิ่มสต็อกติดลบ
def test_add_stock_negative_quantity():
    inv = Inventory()
    with pytest.raises(ValueError, match="cannot be negative"):
        inv.add_stock("Apple", -5)
