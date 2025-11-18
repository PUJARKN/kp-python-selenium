import pytest
from selenium import webdriver
import chromedriver_autoinstaller
import os
from selenium.webdriver.chrome.options import Options
from Utilities.env_loader import Env

# Suppress TensorFlow and other library logs (if used)
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # suppress TF INFO/WARNING


def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome", help="Browser: chrome or firefox"
    )


@pytest.fixture(scope="session")
def aws_credentials():
    """
    Fixture to provide AWS credentials from environment variables.
    """

    username = ${{ secrets.AWS_USERNAME }}
    password = ${{ secrets.AWS_PASSWORD }}
    account_id = ${{ secrets.EMAIL_FROM }}

    if not username or not password:
        raise ValueError("AWS_USERNAME or AWS_PASSWORD not set in environment variables!")

    return {
        "username": username,
        "password": password,
        "account_id": account_id
    }


@pytest.fixture(scope='function')
def driver():
    """
    Returns a Chrome WebDriver instance with suppressed logs.
    Each test gets its own driver instance.
    """
    chromedriver_autoinstaller.install()

    chrome_options = Options()
    # Suppress DevTools and verbose logging
    chrome_options.add_argument("--log-level=3")
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    chrome_options.add_argument("--disable-extensions")
    chrome_options.add_argument("--disable-logging")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--silent")
    # chrome_options.add_argument("--headless")  # optional: run tests headless
    chrome_options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    yield driver
    driver.quit()
