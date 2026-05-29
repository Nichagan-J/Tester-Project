import pytest
import json
import os

@pytest.fixture(scope="session")
def test_data():
    data_path = os.path.join(os.path.dirname(__file__), 'fixtures', 'test-data.json')
    with open(data_path) as f:
        return json.load(f)

# The `page` fixture is automatically provided by pytest-playwright.
# You can customize context and browser launch options via pytest command line args 
# e.g., pytest --headed --browser=chromium
