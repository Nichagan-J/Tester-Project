# Checkout & Payment Test Cases

## Module: Checkout Process
**Test Environment:** Windows 11, Chrome 120.0  

| Test Case ID | Test Scenario | Pre-conditions | Steps to Execute | Expected Results | Actual Results | Status |
|-------------|---------------|----------------|------------------|------------------|----------------|--------|
| TC_PAY_001 | Proceed to checkout with items | User is on `cart.html` and has at least 1 item in the cart. | 1. Click "Checkout (Proceed to Payment)" button. | System redirects to `payment.html` and displays payment setup for the correct number of items. | Redirected to payment successfully. Success message shown. | Pass |
| TC_PAY_002 | Proceed to checkout with empty cart | User is on `cart.html` and has 0 items in the cart. (Empty Cart state) | 1. Click "Checkout (Proceed to Payment)" button. | System should disable the Checkout button or display an error message to prevent checkout. | System redirects to `payment.html` despite having 0 items in the cart. | Fail (Bug-001) |

## Module: Payment Display
| Test Case ID | Test Scenario | Pre-conditions | Steps to Execute | Expected Results | Actual Results | Status |
|-------------|---------------|----------------|------------------|------------------|----------------|--------|
| TC_PAY_003 | View payment setup page | User has successfully checked out with items. | 1. View `payment.html`. | System shows "Please enter payment details for X item(s)." | Correct items count displayed. | Pass |
