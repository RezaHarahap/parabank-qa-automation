import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

BASE_URL = os.getenv("PARABANK_BASE_URL", "https://parabank.parasoft.com/parabank").rstrip("/")

@pytest.fixture

def base_url():
    return BASE_URL

@pytest.fixture

def driver():
    options = Options()
    if os.getenv("HEADLESS", "true").lower() in {"1", "true", "yes"}:
        options.add_argument("--headless=new")
    options.add_argument("--window-size=1440,1000")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--no-sandbox")
    browser = webdriver.Chrome(options=options)
    browser.implicitly_wait(2)
    yield browser
    browser.quit()
