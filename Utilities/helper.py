import os
import time
import glob
import pytesseract
from PIL import Image

folder_path = r'C:\Kapil\Work\Coding\Pytest_Selenium\pages\screenshot'


def take_screenshot(driver, name):
    folder = "pages/screenshot"
    os.makedirs(folder, exist_ok=True)

    timestamp = time.strftime("%Y%m%d-%H%M%S")
    filename = f"{folder}/{name}_{timestamp}.png"

    driver.save_screenshot(filename)
    return filename


# ----------------------------
# Configure Tesseract executable path
# ----------------------------
# Change this to where you installed/extracted Tesseract
# Example: r"C:\Kapil\Tesseract-OCR\tesseract.exe"


def get_latest_billing_screenshot(folder_path):
    """
    Returns the full path of the latest PNG screenshot whose filename contains 'AWS Billing'.
    """
    # Get all PNG files in folder
    png_files = glob.glob(os.path.join(folder_path, "*.png"))
    if not png_files:
        print("❌ No PNG files found in folder")
        return None

    # Filter files containing 'AWS Billing' in filename
    billing_files = [f for f in png_files if "AWS Billing" in os.path.basename(f)]
    if not billing_files:
        print("❌ No screenshot filename contains 'AWS Billing'")
        return None

    # Return the latest modified file
    latest_file = max(billing_files, key=os.path.getmtime)
    print(f"✔ Latest screenshot found: {latest_file}")
    return latest_file
