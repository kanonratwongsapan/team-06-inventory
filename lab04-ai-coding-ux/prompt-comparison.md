# การเปรียบเทียบ Prompt Engineering vs Context Engineering
Lab 04 - ขั้นที่ 7

## รอบที่ 1: สั่งงานด้วย Prompt เปล่า (ไม่มี Context)
**คำสั่งที่ใช้ (Prompt):** 
> "เขียนฟังก์ชันภาษา Python สำหรับลดสต๊อกสินค้าให้หน่อย"

**ผลลัพธ์ที่ AI สร้างให้ (จำลอง):**
```python
def decrease_stock(product_id, amount, current_stock):
    if amount <= 0:
        return "Amount must be greater than zero."
    if current_stock < amount:
        return "Error: Not enough stock."
    
    new_stock = current_stock - amount
    print(f"Product {product_id} stock reduced by {amount}. New stock: {new_stock}")
    return new_stock