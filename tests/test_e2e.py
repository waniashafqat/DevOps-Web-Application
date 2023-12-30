from selenium import webdriver
import pytest

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

def test_submit_data(browser):
    browser.get("http://localhost:5000")
    input_field = browser.find_element_by_id("userData")
    submit_button = browser.find_element_by_css_selector("button.submit-btn")
    
    input_field.send_keys("Test Data")
    submit_button.click()

    
