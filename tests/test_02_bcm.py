from pages.login_page import LoginPage
from pages.Billing_Cost_Management import BCMPage
from Utilities.config import BASE_URL
import os
import pytest


# @pytest.mark.skip("Not implemented yet on git hub")
def test_bcm_module(driver,):
    driver.get(BASE_URL)

    # Step 1: Login
    login = LoginPage(driver)
    login.login_credential()

    assert login.is_login_successful(), "Login failed!"

    # Step 2: BCM Page actions
    bcm = BCMPage(driver)

    bcm.validate_bcm_page_loaded()
    bcm.search_bcm("Billing and Cost Management", screenshot_name="bcm_page")
