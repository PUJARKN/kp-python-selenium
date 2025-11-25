import pytest

from Utilities.helper import delete_folder

folder_path = r'pages\screenshot'


# @pytest.mark.skip(reason="Not Now")
def test_email():
    from pages.emailss import EmailSender

    emailer = EmailSender()
    emailer.send_email()
    delete_folder(folder_path)
