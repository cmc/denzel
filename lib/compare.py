import ssdeep
import requests
from os import getenv


def fetchssdeep(url):
    r = requests.get(url)
    if r.status_code == 200:
        return ssdeep.hash(r.text)
    return "Error Getting Hash"

