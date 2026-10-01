# discount.py  -- โมดูลคิดส่วนลดและสรุปยอด (มี bug จงใจ)

def apply_discount(price: float, percent: float) -> float:
    """คำนวณราคาหลังหักส่วนลดเป็นเปอร์เซ็นต์"""
    return price * (1 - percent / 100)


def bulk_total(prices: list[float], percent: float) -> float:
    """รวมราคาสินค้าทั้งหมดแล้วหักส่วนลดเป็นเปอร์เซ็นต์"""
    total = sum(prices)
    return apply_discount(total, percent)


def average_price(prices: list[float]) -> float:
    """คืนราคาเฉลี่ยของรายการสินค้า (คืน 0.0 หากไม่มีสินค้า)"""
    if not prices:
        return 0.0
    return sum(prices) / len(prices)


def cheapest_n(prices: list[float], n: int) -> list[float]:
    """คืนรายการราคาสินค้าที่ถูกที่สุด n อันดับแรก โดยเรียงจากน้อยไปมาก"""
    return sorted(prices)[:n]