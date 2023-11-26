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


def test_step1(coord01, text01):
    assert text01 in get_sites(coord01[0], coord01[1], 100), "Site not found"
