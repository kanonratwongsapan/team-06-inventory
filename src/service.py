from typing import Dict, List
from src.models import Product
from src.notifiers import Notifier

class InventoryService:
    """คลาสสำหรับจัดการ Business Logic ของระบบสินค้าคงคลัง"""
    def __init__(self, notifiers: List[Notifier]):
        self.products: Dict[str, Product] = {}
        self.notifiers = notifiers

    def add_product(self, product: Product) -> None:
        """เพิ่มสินค้าใหม่เข้าสู่ระบบ"""
        self.products[product.name] = product

    def issue_product(self, name: str, qty: int) -> bool:
        """จ่ายสินค้าออกจากสต็อก และแจ้งเตือนหากต่ำกว่า threshold"""
        if name not in self.products:
            return False
        
        product = self.products[name]
        if product.quantity < qty:
            raise ValueError("สต็อกไม่เพียงพอ")
            
        product.quantity -= qty
        
        if product.quantity < product.threshold:
            self._notify_managers(f"สต็อกต่ำ: {product.name} เหลือ {product.quantity}")
        return True

    def _notify_managers(self, message: str) -> None:
        """ส่งแจ้งเตือนไปยัง notifier ทั้งหมด"""
        for notifier in self.notifiers:
            notifier.send(message)

    def get_inventory_value_by_category(self) -> Dict[str, float]:
        """คำนวณมูลค่าสต็อกรวมแยกตามหมวดหมู่"""
        report = {}
        for product in self.products.values():
            if product.category not in report:
                report[product.category] = 0.0
            report[product.category] += product.quantity * product.price
        return report