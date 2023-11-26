import pytest
import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


@pytest.fixture()
def take_token():
    result_post = requests.post(url=data["login_url"],
                                data={"username": data["login"],
                                      "password": data["password"]})
    return result_post.json()["token"]


@pytest.fixture()
def sort_key():
    return "id"


@pytest.fixture()
def find_key():
    return "89681"


@pytest.fixture()
def title():
    return "title01"


@pytest.fixture()
def description():
    return "description01"


@pytest.fixture()
def content():
    return "content01"
