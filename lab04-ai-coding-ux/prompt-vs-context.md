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

## รอบที่ 2: สั่งงานด้วย Prompt + Context
คำสั่งที่ใช้ (Prompt + Context):

"เขียนฟังก์ชันภาษา Python สำหรับลดสต๊อกสินค้าให้หน่อย

Context:

ใช้ signature เดิม: decrease_stock(product_id, amount, current_stock)

ห้าม print

ถ้าสต๊อกไม่พอให้คืนค่า None

ถ้า amount <= 0 ให้คืนค่า None

ต้องคืนค่า stock ใหม่เป็นจำนวนเต็ม"

ผลลัพธ์ที่ AI สร้างให้ (จำลอง):


def decrease_stock(product_id, amount, current_stock):
    """
    ลดสต๊อกสินค้าตามจำนวนที่ระบุ

    Args:
        product_id: รหัสสินค้า
        amount: จำนวนที่ต้องการลด
        current_stock: จำนวนสต๊อกปัจจุบัน

    Returns:
        int | None: จำนวนสต๊อกใหม่ ถ้าไม่สามารถลดได้ให้คืนค่า None
    """
    if amount <= 0:
        return None

    if current_stock < amount:
        return None

    return int(current_stock - amount)

## สรุปความต่าง
รอบที่ 1 ได้โค้ดที่มี print และคืนข้อความ string บางกรณี ทำให้ไม่สอดคล้องกับการใช้งานเป็นฟังก์ชันทั่วไป

รอบที่ 2 โค้ดตรงตามข้อกำหนดมากกว่า เพราะไม่ print, ใช้ None เมื่อทำไม่ได้ และคืนค่าเป็นจำนวนเต็มตามที่กำหนด

สาเหตุที่ต่างกันคือ Context ช่วยบอกข้อจำกัดของฟังก์ชันและรูปแบบค่าที่ต้องคืน ทำให้ AI ตอบได้ตรงโจทย์มากขึ้น