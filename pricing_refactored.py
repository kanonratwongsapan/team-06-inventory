"""โมดูลคำนวณราคาและส่วนลดที่จัดระเบียบโค้ดใหม่ (Refactored) โดยคงพฤติกรรมเดิมทุกประการ"""

 BULK_TIER_HIGH_QTY = 50
BULK_TIER_HIGH_RATE = 0.90
BULK_TIER_LOW_QTY = 10
BULK_TIER_LOW_RATE = 0.95
MEMBER_DISCOUNT_RATE = 0.95

H: list[dict] = []
P: dict[str, int] = {}


def _calculate_item_subtotal(price: float, quantity: int) -> float:
    if quantity <= 0:
        return 0.0
    subtotal = price * quantity
    if quantity >= BULK_TIER_HIGH_QTY:
        return subtotal * BULK_TIER_HIGH_RATE
    if quantity >= BULK_TIER_LOW_QTY:
        return subtotal * BULK_TIER_LOW_RATE
    return subtotal


def _apply_coupon(total: float, coupon: str | None, date_str: str) -> float:
    if coupon is None:
        return total
    if coupon == "SAVE50":
        return total - 50
    if coupon == "VIP10":
        return total * 0.90
    if coupon == "NEWYEAR" and date_str == "2026-01-01":
        return total - 100
    return total


def calc(
    items: list[dict],
    m: str | None = None,
    c: str | None = None,
    dt: str = "2026-10-03",
) -> float:
    total = sum(_calculate_item_subtotal(item["p"], item["q"]) for item in items)

    if m is not None:
        total *= MEMBER_DISCOUNT_RATE

    total = _apply_coupon(total, c, dt)
    total = round(total, 2)

    if m is not None:
        points = int(total // 10) if total > 0 else 0
        P[m] = P.get(m, 0) + points

    H.append({"m": m, "t": total, "len": len(H) + 1})
    return total
