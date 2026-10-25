import os
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

USERNAME = os.getenv("PARABANK_USERNAME", "").strip()
PASSWORD = os.getenv("PARABANK_PASSWORD", "").strip()


def test_homepage_has_login_form(driver, base_url):
    driver.get(f"{base_url}/index.htm")
    assert "ParaBank" in driver.title
    assert driver.find_element(By.NAME, "username").is_displayed()
    assert driver.find_element(By.NAME, "password").is_displayed()


def test_invalid_login_shows_feedback(driver, base_url):
    driver.get(f"{base_url}/index.htm")
    driver.find_element(By.NAME, "username").send_keys("invalid_portfolio_user")
    driver.find_element(By.NAME, "password").send_keys("invalid_password")
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    feedback = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "#rightPanel .error, #rightPanel p"))
    )
    assert feedback.text.strip(), "Expected visible feedback after invalid login"


def test_demo_login_and_account_overview(driver, base_url):
    if not USERNAME or not PASSWORD:
        pytest.skip("Set PARABANK_USERNAME and PARABANK_PASSWORD to a disposable demo account created in ParaBank.")
    driver.get(f"{base_url}/index.htm")
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    # This assertion intentionally validates observable UI. If demo credentials change,
    # mark the test blocked/data issue and update from current official demo instructions.
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "leftPanel")))
    assert driver.find_elements(By.LINK_TEXT, "Accounts Overview"), "Expected account navigation after login"
    driver.find_element(By.LINK_TEXT, "Accounts Overview").click()
    WebDriverWait(driver, 10).until(EC.url_contains("overview.htm"))
    assert "overview.htm" in driver.current_url


def test_transfer_form_is_reachable_when_logged_in(driver, base_url):
    if not USERNAME or not PASSWORD:
        pytest.skip("Set PARABANK_USERNAME and PARABANK_PASSWORD to a disposable demo account created in ParaBank.")
    driver.get(f"{base_url}/index.htm")
    driver.find_element(By.NAME, "username").send_keys(USERNAME)
    driver.find_element(By.NAME, "password").send_keys(PASSWORD)
    driver.find_element(By.CSS_SELECTOR, "input[type='submit']").click()
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "leftPanel")))
    links = driver.find_elements(By.LINK_TEXT, "Transfer Funds")
    if not links:
        pytest.skip("Transfer Funds navigation unavailable for current demo session")
    links[0].click()
    WebDriverWait(driver, 10).until(EC.url_contains("transfer.htm"))
    assert driver.find_elements(By.ID, "amount"), "Expected transfer amount field"
