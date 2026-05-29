import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from pages.login_page import LoginPage
from playwright_config import Config

def test_valid_login(page, test_data):
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    
    user = test_data["valid_user"]
    login_page.login(user["username"], user["password"])
    
    # Assert successful login
    assert "inventory.html" in page.url

def test_invalid_login(page, test_data):
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    
    user = test_data["invalid_user"]
    login_page.login(user["username"], user["password"])
    
    # Assert error message appears
    assert login_page.error_message.is_visible()
