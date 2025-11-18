# pages/login_page.py

import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from Utilities.helper import take_screenshot
from Utilities import logger
from Utilities.env_loader import Env

log = logger.get_logger()


class LoginPage:
    def __init__(self, driver):
        """Initialize with Selenium driver"""
        self.driver = driver

    def login_credential(self, aws_credentials: dict | None = None):
        """
        Performs AWS login using either:
        - `aws_credentials` dict with keys: username, password, account_id
        - or fallback to Env variables if `aws_credentials` is None
        """
        creds = aws_credentials or {
            "username": ${{ secrets.AWS_USERNAME }},
            "password": ${{ secrets.AWS_PASSWORD }},
            "account_id": ${{ secrets.AWS_ACCOUNT_ID }}
        }

        username = creds.get("username")
        password = creds.get("password")
        account_id = creds.get("account_id")

        if not username or not password or not account_id:
            raise ValueError("AWS credentials incomplete!")

        log.info(f"Logging in with IAM user: {username}")

        # Click on Sign-In button
        signin_nav = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="global-nav-desktop"]/div[2]/div/ul[2]/li[2]/a/div')
            )
        )
        signin_nav.click()

        # Enter Account ID
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'account'))
        ).send_keys(account_id)

        # Enter IAM Username
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, 'username'))
        ).send_keys(username)

        # Enter Password
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, 'password'))
        ).send_keys(password)

        # Click Sign In
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.ID, 'signin_button'))
        ).click()

    def is_login_successful(self, screenshot_name: str | None = None, timeout: int = 15) -> bool:
        """Returns True if Console Home heading appears within `timeout` seconds"""
        try:
            log.info("Waiting for Console Home heading to appear...")
            time.sleep(4)
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.ID, "awsc-concierge-input"))
            )
            log.info("Console Home found — login successful.")
            return True
        except TimeoutException:
            log.warning("Console Home did not appear within timeout")
            return False
