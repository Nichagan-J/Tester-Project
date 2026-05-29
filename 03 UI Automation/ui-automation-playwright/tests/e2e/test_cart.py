import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from pages.cart_page import CartPage
from playwright_config import Config

def test_add_product_to_cart(page, test_data):
    # 1. Login
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    login_page.login(test_data["valid_user"]["username"], test_data["valid_user"]["password"])
    
    # 2. Add product to cart
    product_page = ProductPage(page)
    product_name = test_data["product"]
    product_page.add_to_cart(product_name)
    
    # 3. Go to cart and verify
    product_page.go_to_cart()
    cart_page = CartPage(page)
    assert cart_page.verify_item_in_cart(product_name) is True

def test_remove_product_from_cart(page, test_data):
    # 1. Login
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    login_page.login(test_data["valid_user"]["username"], test_data["valid_user"]["password"])
    
    # 2. Add product to cart
    product_page = ProductPage(page)
    product_name = test_data["product"]
    product_page.add_to_cart(product_name)
    
    # 3. Go to cart
    product_page.go_to_cart()
    cart_page = CartPage(page)
    
    # 4. Remove item and verify cart is empty
    cart_page.remove_item(product_name)
    assert cart_page.is_cart_empty() is True
    assert cart_page.verify_item_in_cart(product_name) is False

