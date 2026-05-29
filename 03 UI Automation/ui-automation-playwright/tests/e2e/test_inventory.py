import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from pages.login_page import LoginPage
from pages.product_page import ProductPage
from playwright_config import Config

def test_sort_products_by_price_low_to_high(page, test_data):
    # 1. Login
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    login_page.login(test_data["valid_user"]["username"], test_data["valid_user"]["password"])
    
    # 2. Sort products
    product_page = ProductPage(page)
    product_page.sort_products_by("lohi") # lohi = Price (low to high)
    
    # 3. Verify sorting logic (prices should be in ascending order)
    prices = product_page.get_all_product_prices()
    assert prices == sorted(prices), f"Expected prices to be sorted ascending, but got {prices}"

def test_sort_products_by_price_high_to_low(page, test_data):
    # 1. Login
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    login_page.login(test_data["valid_user"]["username"], test_data["valid_user"]["password"])
    
    # 2. Sort products
    product_page = ProductPage(page)
    product_page.sort_products_by("hilo") # hilo = Price (high to low)
    
    # 3. Verify sorting logic (prices should be in descending order)
    prices = product_page.get_all_product_prices()
    assert prices == sorted(prices, reverse=True), f"Expected prices to be sorted descending, but got {prices}"
