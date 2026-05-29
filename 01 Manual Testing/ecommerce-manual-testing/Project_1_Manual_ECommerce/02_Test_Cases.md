# Test Cases Design

## Scenario 1: Login Functionality
| Test Case ID | Description | Steps to Reproduce | Expected Result | Type |
|--------------|-------------|--------------------|-----------------|------|
| TC01 | Login with valid credentials | 1. ไปที่หน้า Login 2. กรอก User/Pass ที่ถูกต้อง 3. กด Login | เข้าสู่หน้า Dashboard สำเร็จ | Positive |
| TC02 | Login with invalid password | 1. ไปที่หน้า Login 2. กรอก User ถูก แต่ Pass ผิด 3. กด Login | แสดง Error message "Invalid credentials" | Negative |
| TC03 | Login with empty fields | 1. ไปที่หน้า Login 2. ปล่อยว่าง 3. กด Login | แสดง Error message แจ้งเตือนให้กรอกข้อมูล | Edge Case |

## Scenario 2: Add to Cart
| Test Case ID | Description | Steps to Reproduce | Expected Result | Type |
|--------------|-------------|--------------------|-----------------|------|
| TC04 | Add item to cart | 1. ไปที่หน้า Dashboard 2. กด Add to Cart สินค้า 3. ไปที่ Cart | สินค้าที่เลือกแสดงในตะกร้า | Positive |

## Scenario 3: Checkout Process
| Test Case ID | Description | Steps to Reproduce | Expected Result | Type |
|--------------|-------------|--------------------|-----------------|------|
| TC05 | Checkout with items | 1. ไปที่กล่อง Cart (มีสินค้า) 2. กด Checkout | ไปยังหน้า Payment สำเร็จ | Positive |
| TC06 | Checkout with empty cart | 1. ไปที่ Cart (ไม่มีสินค้า) 2. กด Checkout | ระบบแจ้งเตือน ไม่พาไปหน้า Payment | Negative/Edge Case |

## Scenario 4: Payment
| Test Case ID | Description | Steps to Reproduce | Expected Result | Type |
|--------------|-------------|--------------------|-----------------|------|
| TC07 | View payment with valid cart | 1. ผ่านจาก Checkout มายัง Payment | แสดงข้อความให้ชำระเงินตามจำนวนสินค้า | Positive |