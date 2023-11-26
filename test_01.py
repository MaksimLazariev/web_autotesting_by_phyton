"""
    geosearch.py
    MediaWiki API Demos
    Demo of `Geosearch` module: Search for wiki pages nearby
    MIT License
"""

import requests

S = requests.Session()


def get_sites(latitude, longitude, radius, limit=100):
    URL = "https://en.wikipedia.org/w/api.php"
    PARAMS = {
        "format": "json",
        "list": "geosearch",
        "gscoord": f"{latitude}|{longitude}",
        "gslimit": f"{limit}",
        "gsradius": f"{radius}",
        "action": "query"
    }
    r = S.get(url=URL, params=PARAMS)
    pages = r.json()['query']['geosearch']
    sites = [i["title"] for i in pages]
    return sites


def test_step1():
    assert "One Montgomery Tower" in get_sites("37.7891838", "-122.4033522",
                                               100), "Site not found"


test_step1()
