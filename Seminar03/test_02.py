from testpage import OperationsHelper
import logging
import time
import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step01(browser):
    # Login
    logging.info("Test_02.step_01 started")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.open_the_site()
    testpage.enter_login("test")
    testpage.enter_password("test")
    testpage.click_login_button()
    time.sleep(testdata["sleep_time"])
    # Take Error
    assert testpage.get_error_text() == "401"


def test_step02(browser, login_result):
    # Login
    logging.info("Test_02.step_02 started")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.open_the_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_password(testdata["password"])
    testpage.click_login_button()
    time.sleep(testdata["sleep_time"])
    # Take Result
    assert testpage.get_login_text() == login_result


def test_step03(browser):
    # Login
    logging.info("Test_02.step_03 started")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.open_the_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_password(testdata["password"])
    testpage.click_login_button()
    time.sleep(testdata["sleep_time"])
    # post creation
    testpage.click_create_post_button()
    testpage.enter_post_title(testdata["title"])
    testpage.enter_post_description(testdata["description"])
    testpage.enter_post_content(testdata["content"])
    testpage.click_save_post_button()
    time.sleep(testdata["sleep_time"])
    # Take post title
    assert testpage.get_new_post_text() == testdata["title"]


def test_step04(browser):
    # Login
    logging.info("Test_02.step_04 started")
    testpage = OperationsHelper(browser, testdata["address"])
    testpage.open_the_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_password(testdata["password"])
    testpage.click_login_button()
    time.sleep(testdata["sleep_time"])
    # Open and sent Contact us
    testpage.click_contact_us_button()
    testpage.enter_feedback_name(testdata["login"])
    testpage.enter_feedback_email(testdata["e-mail"])
    testpage.enter_feedback_content(testdata["content"])
    testpage.click_feedback_sent_button()
    time.sleep(testdata["sleep_time"])
    # Take Result
    assert testpage.get_alert() == "Form successfully submitted"

