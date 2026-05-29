import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from playwright_config import Config

def test_checkout_flow(page, test_data):
    # 1. Login
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    login_page.login(test_data["valid_user"]["username"], test_data["valid_user"]["password"])
    
    # 2. Add product
    product_page = ProductPage(page)
    product_page.add_to_cart(test_data["product"])
    product_page.go_to_cart()
    
    # 3. Checkout
    cart_page = CartPage(page)
    cart_page.proceed_to_checkout()
    
    # 4. Fill checkout info (Simplified for Demo)
    page.locator("[data-test='firstName']").fill("Test")
    page.locator("[data-test='lastName']").fill("User")
    page.locator("[data-test='postalCode']").fill("12345")
    page.locator("[data-test='continue']").click()
    
    # 5. Finish
    page.locator("[data-test='finish']").click()
    assert page.locator(".complete-header").is_visible()
