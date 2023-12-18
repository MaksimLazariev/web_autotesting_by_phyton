import pytest
import requests
import yaml


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from email_report import send_email

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


@pytest.fixture(scope="function")
def browser():
    driver = None
    if testdata["browser"] == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options)
    elif testdata["browser"] == "chrome":
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()


@pytest.fixture()
def login_result():
    return """Home"""


@pytest.fixture(scope="session")
def send_report():
    yield
    send_email()


@pytest.fixture()
def take_token():
    result_post = requests.post(url=testdata["login_url"],
                                data={"username": testdata["login"],
                                      "password": testdata["password"]})
    return result_post.json()["token"]


# @pytest.fixture()
# def sort_key():
#     return "id"
#
#
# @pytest.fixture()
# def find_key():
#     return "93049"
#
#
# @pytest.fixture()
# def title():
#     return "title01"
#
#
# @pytest.fixture()
# def description():
#     return "description01"
#
#
# @pytest.fixture()
# def content():
#     return "content01"
