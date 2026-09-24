from dataclasses import dataclass
from typing import Literal

@dataclass
class Product:
    """ตัวแทนของสินค้าในระบบ"""
    name: str
    category: str
    price: float
    quantity: int
    threshold: int