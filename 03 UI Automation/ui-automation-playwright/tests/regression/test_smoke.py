import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from pages.login_page import LoginPage
from playwright_config import Config

def test_smoke_login_page_loads(page):
    login_page = LoginPage(page)
    login_page.navigate(Config.BASE_URL)
    
    # Verify we are on the login page
    assert page.title() == "Swag Labs"
    assert login_page.login_button.is_visible()
