import pytest
import yaml
from module import Site

# with open("selenium/testdata.yaml") as f:
with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


@pytest.fixture()
def login_xpath():
    return """//*[@id="login"]/div[1]/label/input"""


@pytest.fixture()
def password_xpath():
    return """//*[@id="login"]/div[2]/label/input"""


@pytest.fixture()
def button_xpath():
    return """//*[@id="login"]/div[3]/button"""


@pytest.fixture()
def error_xpath():
    return """//*[@id="app"]/main/div/div/div[2]/h2"""


@pytest.fixture()
def error_code():
    return "401"


@pytest.fixture()
def login_result_xpath():
    return """//*[@id="app"]/main/nav/a/span"""


@pytest.fixture()
def login_result():
    return """Home"""


@pytest.fixture()
def create_button_xpath():
    return """//*[@id="create-btn"]"""


@pytest.fixture()
def title_xpath():
    return """//*[@id="create-item"]/div/div/div[1]/div/label/input"""


@pytest.fixture()
def description_xpath():
    return """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea"""


@pytest.fixture()
def content_xpath():
    return """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea"""


@pytest.fixture()
def save_button_xpath():
    return """//*[@id="create-item"]/div/div/div[7]/div/button"""


@pytest.fixture()
def created_post_title_css():
    return """h1"""


@pytest.fixture()
def site():
    browser = Site(testdata["address"])
    yield browser
    browser.close()
