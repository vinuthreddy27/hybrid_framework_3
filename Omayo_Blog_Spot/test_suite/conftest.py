import pytest
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(autouse=True)
def driver():
    driver=WebDriver()
    chrome_options=Options()
    chrome_options.add_argument("--disable notifications")
    driver.get("https://omayo.blogspot.com/")
    # driver.get("https://only-testing-blog.blogspot.com/2014/01/textbox.html")
    driver.maximize_window()
    yield driver
    driver.quit()
