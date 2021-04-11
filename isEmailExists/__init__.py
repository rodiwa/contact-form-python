# This function is not intended to be invoked directly. Instead it will be
# triggered by an orchestrator function.
# Before running this sample, please:
# - create a Durable orchestration function
# - create a Durable HTTP starter function
# - add azure-functions-durable to requirements.txt
# - run pip install -r requirements.txt

import logging
from validate_email import validate_email


def main(name: str) -> str:
    email = name['email']
    isEmailExists = validate_email(email_address=email)
    return isEmailExists
