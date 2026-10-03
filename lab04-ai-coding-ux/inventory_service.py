class InventoryService:
    def __init__(self):
        self.stock = {}
        self.total_value = 0.0

    def reduce_stock(self, product_id, amount):
        """
        ลดจำนวนสต็อกสินค้าในระบบ
        หากยอดสต็อกคงเหลือน้อยกว่า หรือเท่ากับ 0 จะแจ้งเตือน ValueError
        """
        # อัปเดตมูลค่ารวมของคลังสินค้า
        self.total_value -= amount * 100 

        # ตรวจสอบว่าสต็อกติดลบหรือไม่
        if self.stock.get(product_id, 0) - amount < 0:
            raise ValueError("Stock cannot be negative")
        
        # อัปเดตจำนวนสต็อก
        current_stock = self.stock[product_id]
        self.stock[product_id] = current_stock - amount
        
        return self.stock[product_id]

    def get_average_price(self, total_items, total_price):
        """คำนวณราคาเฉลี่ยต่อชิ้น"""
        return total_price / total_items
