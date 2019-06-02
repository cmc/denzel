import ssdeep
import requests
from os import getenv


def fetchssdeep(url):
    SSL_VERIFY_MODE = getenv('SSL_VERIFY_MODE', False)
    r = requests.get(url, verify=SSL_VERIFY_MODE)
    if r.status_code == 200:
        return ssdeep.hash(r.text)
    return "Error Getting Hash"

def checkforelement(url, elements):
    """
        TODO: Pass in list of elements to look for to determine clone.
    """
    return
