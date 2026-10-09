@'
# โครงงานระบบจัดการคลังสินค้า (Inventory Management System) - Team 06

## ภาพรวมโครงการ (Project Overview)
โครงงานนี้เป็นการพัฒนาระบบจัดการคลังสินค้าขนาดเล็กที่สร้างขึ้นเพื่อประยุกต์ใช้หลักการวิศวกรรมซอฟต์แวร์ (Software Engineering) และการใช้ AI มาช่วยในการพัฒนาอย่างเป็นระบบ โดยครอบคลุมตั้งแต่การออกแบบ UX/UI, การทำ Code Review, การเขียน Unit Test ด้วยแนวคิด TDD (Test-Driven Development), การทำ Refactoring โค้ดเก่า และการวางระบบ CI/CD (Continuous Integration / Continuous Deployment)

## ฟีเจอร์หลัก (Key Features)
- **จัดการสต็อกสินค้า:** ระบบสามารถเพิ่มสต็อก (Add) และตัดสต็อก (Sell) สินค้าได้ พร้อมระบบป้องกันข้อผิดพลาด เช่น ยอดสต็อกติดลบ หรือการป้อนชนิดข้อมูลผิด
- **แจ้งเตือนสต็อกต่ำ (Low Stock Alert):** ค้นหาและดึงรายการสินค้าที่มีจำนวนคงเหลือน้อยกว่าหรือเท่ากับเกณฑ์ที่กำหนด เพื่อเตรียมสั่งซื้อเพิ่ม
- **คำนวณราคาและส่วนลด (Pricing Module):** ระบบรองรับการคิดราคาสินค้า, ส่วนลดจากการซื้อจำนวนมาก (Bulk discount), การหักคูปองส่วนลด และการคำนวณแต้มสะสมสำหรับสมาชิก
- **รองรับสินค้า 2 ประเภท:** รองรับกฎเกณฑ์ที่แตกต่างกันระหว่างสินค้าที่จับต้องได้ (Physical Product) และสินค้าดิจิทัล (Digital Product)

## เครื่องมือและเทคโนโลยีที่ใช้ (Tech Stack)
- **ภาษาหลัก:** Python 3.11+
- **Testing Framework:** Pytest และ Pytest-cov (สำหรับวัด Code Coverage)
- **Code Linter:** Ruff
- **CI/CD Pipeline:** GitHub Actions

## สมาชิกในทีม (Team 06)
- พัฒนาและดูแลระบบโดย: Team 06 (รายวิชา Software Engineering in AI Era)
'@ | Set-Content -Path PROJECT.md -Encoding utf8

git add PROJECT.md
git commit -m "docs: create PROJECT.md with comprehensive project overview"
git push origin main
