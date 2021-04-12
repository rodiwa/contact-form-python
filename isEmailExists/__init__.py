import logging
from validate_email import validate_email


def main(name: str) -> str:
    """To check if email exists."""
    try:
        email = name['email']
        isEmailExists = validate_email(email_address=email)
        return isEmailExists
    except Exception as error:
        logging.error(error)
