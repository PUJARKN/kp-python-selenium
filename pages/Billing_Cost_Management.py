# pages/bcm_page.py

import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.helper import take_screenshot
from Utilities.logger import get_logger
from selenium.webdriver.common.keys import Keys

logger = get_logger()


class BCMPage:

    def __init__(self, driver):
        self.driver = driver

        # Locator for BCM search field
        self.search_input = (By.ID, "awsc-concierge-input")

        # Expected page title or heading
        self.expected_heading = "Billing and Cost Management home"

    def validate_bcm_page_loaded(self):
        """Validate if BCM Page loaded successfully"""
        logger.info("Validating BCM Page...")

    def search_bcm(self, text, screenshot_name=None):
        """Enter text into BCM search field and select suggestion"""

        logger.info(f"Entering BCM text: {text}")

        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.search_input)
            )

            # Type text in search box
            element.send_keys(text)

            # Select the first option in dropdown\
            time.sleep(1)
            element.send_keys(Keys.ARROW_RIGHT)
            element.send_keys(Keys.ENTER)
            time.sleep(10)
            take_screenshot(self.driver, "AWS Billing")
            logger.info("BCM search performed successfully.")

        except Exception as e:
            take_screenshot(self.driver, screenshot_name)
            logger.error(f"Unable to perform BCM search. Error: {e}")



