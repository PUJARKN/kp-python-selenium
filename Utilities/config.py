import os

# Load environment variables or default values
BASE_URL = os.getenv("BASE_URL", "https://aws.amazon.com/console/")
BROWSER = os.getenv("BROWSER", "chrome")  # chrome / firefox


