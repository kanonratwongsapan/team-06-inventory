import pytest

from pricing_refactored import H, P, calc


@pytest.fixture(autouse=True)
def clear_saved_state():
    """ล้างค่าที่ฟังก์ชันเก็บค้างไว้ใน Global State ก่อนเริ่มทุก test"""
    H.clear()
    P.clear()


# 1. ราคาปกติ: สินค้าหนึ่งรายการ จำนวนน้อย ไม่ใช้สิทธิ์อะไรเลย
def test_normal_price_single_item():
    items = [{"p": 100, "q": 2}]
    assert calc(items) == 200.0


# 2. ซื้อจำนวนมาก: บันทึกค่าที่จำนวนเท่ากับเกณฑ์แต่ละขั้นพอดี (10 ชิ้น และ 50 ชิ้น)
def test_bulk_discount_at_exact_thresholds():
    assert calc([{"p": 100, "q": 10}]) == 950.0
    assert calc([{"p": 100, "q": 50}]) == 4500.0


# 3. จำนวนเป็นศูนย์: สินค้าที่ใส่จำนวน 0 มา
def test_zero_quantity_item():
    assert calc([{"p": 100, "q": 0}]) == 0.0


# 4. สมาชิก: บันทึกทั้งยอดเงินที่คืนมา และแต้มที่สมาชิกได้รับ
def test_member_discount_and_points():
    total = calc([{"p": 100, "q": 2}], m="M001")
    assert total == 190.0
    assert P["M001"] == 19


# 5. คูปอง: ทุกรหัสที่โค้ดรู้จัก รวมทั้งวันที่เข้าเงื่อนไขและวันที่ไม่เข้า
def test_all_coupons_and_dates():
    items = [{"p": 200, "q": 1}]
    assert calc(items, c="SAVE50") == 150.0
    assert calc(items, c="VIP10") == 180.0
    assert calc(items, c="NEWYEAR", dt="2026-01-01") == 100.0
    assert calc(items, c="NEWYEAR", dt="2026-10-03") == 200.0


# 6. ยอดติดลบ: ส่วนลดมากกว่าราคาสินค้า
def test_negative_total_when_discount_exceeds_price():
    total = calc([{"p": 20, "q": 1}], m="M001", c="SAVE50")
    assert total == -31.0
    assert P["M001"] == 0


# 7. ค่าที่ฟังก์ชันเก็บไว้: ตรวจสอบประวัติที่บันทึกไว้ทุกครั้งที่ถูกเรียก
def test_saved_history_state():
    calc([{"p": 50, "q": 1}], m="M001")
    calc([{"p": 30, "q": 1}], m="M002")
    assert len(H) == 2
    assert H[0] == {"m": "M001", "t": 47.5, "len": 1}
    assert H[1] == {"m": "M002", "t": 28.5, "len": 2}
