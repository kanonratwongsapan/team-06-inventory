# AI Iteration Log

| ประเด็น | ก่อนมี context (ขั้นที่ 4) | หลังมี context (ขั้นที่ 6) |
|---|---|---|
| แยกไฟล์/ความรับผิดชอบ | รวมทุกอย่างในไฟล์เดียว คลาสเดียว | แยกเป็น models, notifiers, และ service ชัดเจน |
| type hint + docstring | ไม่มีเลย | มี type hint และ docstring ภาษาไทยทุก public method |
| service ผูกกับ notifier ตรง ๆ หรือไม่ | ผูกตรงๆ ใช้ print ผสมเงื่อนไข if ซ้อนใน method ทันที | ไม่ผูกตรงๆ รับ dependency ผ่าน constructor (DIP) |
| hardcode config หรือไม่ | hardcode ข้อความเตือนและเบอร์โทรใน business logic | ไม่ hardcode โยน config เข้าไปตอนสร้างผ่าน NotifierFactory |

## Iteration 1
* **ผลที่ผิด:** AI ลืมทำ NotifierFactory ในรอบแรก และเขียนโค้ดเพื่อส่งอีเมลจริง
* **สาเหตุ:** AI มองข้ามกฎข้อห้ามบางข้อ (ละเมิด context)[cite: 1]
* **แก้ต้นทางอย่างไร:** ชี้กลับไปที่กฎโดยตอบกลับ prompt ว่า "โค้ดนี้ละเมิด .ai-rules.md ข้อห้ามส่งจริง ให้ใช้ print ตามกฎ"[cite: 1]
* **ผลหลังแก้:** AI สร้าง NotifierFactory สำเร็จ และเปลี่ยนการส่งเมลเป็นการใช้คำสั่ง print แทน[cite: 1]

## Iteration 2
* **ผลที่ผิด:** AI ตีความ "ต่ำกว่า threshold" เป็นเครื่องหมายน้อยกว่าหรือเท่ากับ (<=)[cite: 1]
* **สาเหตุ:** Spec กำกวม[cite: 1]
* **แก้ต้นทางอย่างไร:** เพิ่ม scenario ใน spec ว่ากรณีสต็อกเท่ากับ threshold พอดี ต้องไม่แจ้งเตือน แล้วสั่ง implement ใหม่[cite: 1]
* **ผลหลังแก้:** AI เปลี่ยน Logic เป็นเครื่องหมายน้อยกว่า (<) อย่างถูกต้อง[cite: 1]