# Automated API Testing: Restful-Booker

## ข้อมูลทั่วไป (Project Overview)
โปรเจกต์นี้ได้รับการพัฒนาขึ้นเพื่อการทดสอบระบบ API แบบอัตโนมัติ (Automated API Testing) สำหรับแพลตฟอร์มการจองห้องพัก [Restful-Booker](https://restful-booker.herokuapp.com/) โดยประยุกต์ใช้ **Postman** ในการออกแบบและสร้างกรณีทดสอบ (Test Cases) และใช้ **Newman** สำหรับการรันคำสั่งทดสอบผ่าน Command Line Interface (CLI) รวมถึงการสร้างรายงานผลการทดสอบ (Test Report) ในรูปแบบ HTML ที่มีความสวยงามและอ่านง่าย

การทดสอบครอบคลุมกระบวนการทำงานหลัก (Core Workflows) ของระบบ ได้แก่ การสร้าง Token เพื่อยืนยันตัวตน และระบบการจัดการข้อมูลห้องพัก (Booking CRUD Operations)

---

## โครงสร้างของโปรเจกต์ (Directory Structure)

โปรเจกต์นี้ถูกออกแบบจัดโครงสร้างตามมาตรฐานการทำงานแบบฉบับ QA Automation ดังนี้:

- `collections/` : แหล่งจัดเก็บไฟล์ Postman Collection (ประกอบด้วย API Requests, Data Payloads และ Test Scripts)
- `environments/` : แหล่งจัดเก็บกลุ่มตัวแปรสภาพแวดล้อม (Environment Variables) เช่น `dev`, `staging` เพื่อรองรับการเปลี่ยนเซิร์ฟเวอร์แบบไดนามิก
- `test-scenarios/` : แหล่งบันทึกสถานการณ์การทดสอบ (Test Scenarios) สำหรับอ้างอิงและสื่อสารกับผู้ที่เกี่ยวข้องในทีม
- `scripts/` : แหล่งจัดเก็บสคริปต์ (.sh) เพื่อเป็นทางเลือกในการรันชุดคำสั่ง
- `reports/` : โฟลเดอร์ปลายทางสำหรับเก็บบันทึกรายงานผลการทดสอบเชิงลึก (Test Reports) ทั้งรูปแบบ HTML และ JSON

---

## สิ่งที่ต้องเตรียมพร้อม (Prerequisites)

ก่อนเริ่มต้นใช้งานโปรเจกต์ กรุณาตรวจสอบให้แน่ใจว่าอุปกรณ์ของท่านได้รับการติดตั้งซอฟต์แวร์ดังต่อไปนี้เรียบร้อยแล้ว:
- [Node.js](https://nodejs.org/) (แนะนำให้ใช้เวอร์ชัน LTS)
- `npm` (Node Package Manager ซึ่งจะถูกติดตั้งมาพร้อมกับ Node.js)

---

## การติดตั้ง (Installation)

1. เปิดแอปพลิเคชัน Terminal (หรือ Command Prompt)
2. เปลี่ยนไดเรกทอรีไปยังโฟลเดอร์หลักของโปรเจกต์ (`api-testing-postman`)
3. รันคำสั่งต่อไปนี้เพื่อดาวน์โหลดและติดตั้งชุดเครื่องมือแบบอัตโนมัติ (Newman และ Reporter Plugins):
   ```bash
   npm install
   ```

---

## คำสั่งรันการทดสอบ (Test Execution Commands)

ระบบได้จัดเตรียมชุดคำสั่งสำเร็จรูป (NPM Scripts) ไว้เพื่อความสะดวกในการปฏิบัติงาน โดยสามารถรันผ่าน Terminal ได้ดังต่อไปนี้:

**1. รันเฉพาะการทดสอบระบบยืนยันตัวตน (Authentication Only):**
```bash
npm run test:auth
```

**2. รันเฉพาะการทดสอบระบบจองห้องพัก (Booking CRUD Operations):**
*(การรันคำสั่งนี้รวมไปถึงการประมวลผลและการสร้างรายงานทดสอบ Report)*
```bash
npm run test:booking
```

**3. รันการทดสอบทั้งหมดของระบบ (Run All Tests):**
```bash
npm run test:all
```

---

## การดูรายงานผลการทดสอบ (Test Reporting)

เมื่อกระบวนการทดสอบเสร็จสิ้น ระบบจะทำการสร้างรายงานผลลัพธ์โดยอัตโนมัติ ภายใต้โฟลเดอร์ `reports/` ท่านสามารถเข้าถึงสรุปผลการทดสอบได้ 2 รูปแบบ:

1. **รูปแบบตารางโต้ตอบ (Interactive HTML Report):** 
   - ไฟล์: `reports/newman-report.html`
   - วิธีการใช้งาน: ให้ทำการดับเบิลคลิกเพื่อเปิดไฟล์นี้ผ่าน Web Browser ใดก็ได้ ท่านจะพบกับรายงานที่มีกราฟแสดงผลสวยงามและรายละเอียดการเกิด Error ต่างๆ ย้อนหลัง
2. **รูปแบบข้อมูลดิบ (JSON):** 
   - ไฟล์: `reports/newman-result.json`
   - วิธีการใช้งาน: เหมาะสำหรับการส่งออกข้อมูล (Export) นำไปแสดงผลต่อในระบบ Dashboard หรือ CI/CD Tools โดยอัตโนมัติ

---

> **ข้อเสนอแนะ:** โครงสร้างของโปรเจกต์ฉบับนี้ มีคุณสมบัติพร้อมสำหรับการบูรณาการเข้ากับระบบการทำงานอย่างต่อเนื่อง Continuous Integration / Continuous Deployment (CI/CD) เช่น ระบบ GitHub Actions, GitLab CI/CD หรือ Jenkins ได้ทันที