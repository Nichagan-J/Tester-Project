# Authentication Test Cases

## Module: Login
**Test Environment:** Windows 11, Chrome 120.0  
**Test Data:** Username: `admin`, Password: `1234`

| Test Case ID | Test Scenario | Pre-conditions | Steps to Execute | Expected Results | Actual Results | Status |
|-------------|---------------|----------------|------------------|------------------|----------------|--------|
| TC_AUTH_001 | Login with valid credentials | User is on the login page (`index.html`) | 1. Enter username: "admin"<br>2. Enter password: "1234"<br>3. Click Login button. | System redirects user to the Dashboard page. | Redirected to Dashboard successfully. | Pass |
| TC_AUTH_002 | Login with invalid credentials | User is on the login page (`index.html`) | 1. Enter username: "admin"<br>2. Enter password: "wrong_password"<br>3. Click Login button. | System display error "Invalid credentials. Try admin / 1234". | Error message displayed correctly. | Pass |
| TC_AUTH_003 | Login with empty fields | User is on the login page (`index.html`) | 1. Leave username blank<br>2. Leave password blank<br>3. Click Login button. | System display error "Please fill in all fields". | Blank validation error displayed. | Pass |
