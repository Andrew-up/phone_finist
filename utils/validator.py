import re

regex_url = "^(http[s]?:\/\/)?((25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\.){3}(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9]?[0-9])\/?$"
regex_sip = '^[0-9]{2,5}$'
regex_pass = '^.{3,20}$'


def check_url(url: str):
    if re.search(regex_url, url):
        return True
    return False


def check_sip(sip: str):
    if re.search(regex_sip, sip):
        return True
    return False


def check_password(password: str):
    if re.search(regex_pass, password):
        return True
    return False
