# tests/test_login.py

import pytest
import logging
from Utilities.helper import take_screenshot
from pages.login_page import LoginPage
from Utilities.config import BASE_URL
from Utilities import logger
import os
from dotenv import load_dotenv

log = logger.get_logger()

# Load the .env file
load_dotenv()

# Access environment variables
cred = {
    "myUsername": os.getenv("AWS_USERNAME"),
    "myPassword": os.getenv("AWS_PASSWORD"),
    "myAWSAccount": os.getenv("AWS_ACCOUNT_ID")
}


@pytest.mark.parametrize(
    "iam_username, account_id, aws_password, expect_success",
    [
        (cred["myUsername"], cred["myAWSAccount"],cred["myPassword"],True),
        ("ROb", "FishLand", "25pomo", False),
        ("Ned", "Winterfell", "892da", False),
    ]
)
def test_login(driver, iam_username, account_id, aws_password, expect_success):
    """
    Test AWS Login using POM.
    """

    log.info(f"Starting login test for user: {iam_username}")

    # Open AWS login page
    driver.get(BASE_URL)

    # Create page object instance
    page = LoginPage(driver)

    # Build credentials dict (required by login_credential)
    credentials = {
        "username": iam_username,
        "password": aws_password,
        "account_id": account_id
    }

    # Perform login
    try:
        page.login_credential(credentials)
        log.info(f"Login submitted for user: {iam_username}")

    except Exception as e:
        log.error(f"Error during login for {iam_username}: {e}")
        take_screenshot(driver, name=f"{iam_username}_error")
        pytest.fail(f"Exception during login for {iam_username}: {e}")

    # Validate login
    login_success = page.is_login_successful(screenshot_name=iam_username)

    # Always take a screenshot
    # take_screenshot(driver, name=f"{iam_username}_final")

    # Assertion
    assert login_success == expect_success, f"Login test failed for user: {iam_username}"
