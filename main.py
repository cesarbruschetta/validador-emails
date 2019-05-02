import re

REGEX = r"^([a-z0-9-._]+)@([a-z0-9]+)(\.[a-z]{1,3}){1,2}$"


def filter_email(emails):
    return list(filter(lambda e: re.match(REGEX, e), emails))
