import logging
import sys
import os
import chromedriver_autoinstaller

# -----------------------
# Suppress chromedriver_autoinstaller messages
# -----------------------
sys_stdout_backup = sys.stdout
sys.stdout = open(os.devnull, "w")
chromedriver_autoinstaller.install()
sys.stdout.close()
sys.stdout = sys_stdout_backup

logging.getLogger("chromedriver_autoinstaller").setLevel(logging.WARNING)


# -----------------------
# Create and return a logger
# -----------------------
def get_logger():
    logger = logging.getLogger("selenium-tests")
    if not logger.handlers:  # Avoid adding multiple handlers
        handler = logging.StreamHandler()
        formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        # Also add file handler
        file_handler = logging.FileHandler("test_login.log")
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

        logger.setLevel(logging.INFO)  # Default log level
    return logger
