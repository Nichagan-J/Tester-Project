# Bug Reports (Exploratory Testing Phase)

## Bug-001: ไม่สามารถ Checkout ได้เมื่อมีสินค้า 0 ชิ้นในตะกร้า แต่ระบบไม่แสดง Error
**Severity:** Medium
**Status:** Open
**Environment:** Chrome 120.0
**Steps to Reproduce:**
1. ล็อกอินเข้าสู่ระบบ
2. ไปที่หน้า Cart (โดยยังไม่มีการเพิ่มสินค้า)
3. กดปุ่ม Checkout
**Expected Result:** ระบบควร disable ปุ่ม Checkout หรือแสดงข้อความเตือน
**Actual Result:** ระบบพาไปหน้าจอ Payment แต่ข้อมูลว่างเปล่า
**Attachment:** screenshots/bug-001-empty-checkout.png