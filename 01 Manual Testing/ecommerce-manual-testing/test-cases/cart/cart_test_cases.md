# Cart Management Test Cases

## Module: Add to Cart & Cart Summary
**Test Environment:** Windows 11, Chrome 120.0  
**Pre-requisite:** User must be logged in and on `dashboard.html`.

| Test Case ID | Test Scenario | Pre-conditions | Steps to Execute | Expected Results | Actual Results | Status |
|-------------|---------------|----------------|------------------|------------------|----------------|--------|
| TC_CART_001 | Add items to cart successfully | Cart is initially empty. | 1. Click "Add to Cart" for Laptop ($999)<br>2. Prompt confirms addition.<br>3. Click "Go to Cart" button. | Cart page displays Laptop. Total price is updated to $999. | Item displayed correctly. Total is correct. | Pass |
| TC_CART_002 | Add multiple items to cart | Cart is empty or has items. | 1. Add Laptop<br>2. Add Mouse<br>3. Go to Cart page. | Cart page displays both items. Total price is calculated correctly ($1048). | Items and sum total updated correctly. | Pass |
| TC_CART_003 | View empty cart | User has not added any items. | 1. Navigate directly to "Go to Cart" from Dashboard. | System displays "Empty Cart". Total price is 0. | "Empty Cart" message displayed. Total is 0. | Pass |
