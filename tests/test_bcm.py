from pages.login_page import LoginPage
from pages.Billing_Cost_Management import BCMPage
from Utilities.config import BASE_URL
import os

# Read environment variables if parameters not passed
# iam_username = "kapil"
# account_id = "aws-kapil-1993"
# aws_password = "K@pil007"


def test_bcm_module(driver,aws_credentials):
    driver.get(BASE_URL)

    # Step 1: Login
    login = LoginPage(driver)
    login.login_credential()

    assert login.is_login_successful(), "Login failed!"

    # Step 2: BCM Page actions
    bcm = BCMPage(driver)

    bcm.validate_bcm_page_loaded()
    bcm.search_bcm("Billing and Cost Management", screenshot_name="bcm_page")

