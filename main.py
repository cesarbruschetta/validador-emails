import re

REGEX = r"^([a-z0-9-._]+)@([a-z0-9]+)(\.[a-z]{1,3})+$"


def valid_email(email):
    match = re.match(REGEX, email)
    if match:
        return True
    return False


def filter_email(emails):
    return [email for email in emails if valid_email(email)]
