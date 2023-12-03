import time

import yaml

with open("testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_step01(site, login_xpath, password_xpath, button_xpath, error_xpath,
                error_code):
    # input login
    input01 = site.find_element("xpath", login_xpath)
    input01.send_keys("test")
    # input password
    input02 = site.find_element("xpath", password_xpath)
    input02.send_keys("test")
    # login button click
    btn = site.find_element("xpath", button_xpath)
    btn.click()
    time.sleep(testdata["sleep_time"])
    # get error code
    err_label = site.find_element("xpath", error_xpath)
    assert err_label.text == error_code


def test_02(site, login_xpath, password_xpath, button_xpath,
            login_result_xpath, login_result):
    # input login
    input01 = site.find_element("xpath", login_xpath)
    input01.send_keys(testdata["login"])
    # input password
    input02 = site.find_element("xpath", password_xpath)
    input02.send_keys(testdata["password"])
    # login button click
    btn = site.find_element("xpath", button_xpath)
    btn.click()
    time.sleep(testdata["sleep_time"])
    # get login result
    login_label = site.find_element("xpath", login_result_xpath)
    assert login_label.text == login_result


def test_step03(site, login_xpath, password_xpath, button_xpath,
                create_button_xpath, title_xpath, description_xpath,
                content_xpath, save_button_xpath, created_post_title_css):
    # input login
    input01 = site.find_element("xpath", login_xpath)
    input01.send_keys(testdata["login"])
    # input password
    input02 = site.find_element("xpath", password_xpath)
    input02.send_keys(testdata["password"])
    # login button click
    btn = site.find_element("xpath", button_xpath)
    btn.click()
    time.sleep(testdata["sleep_time"])
    # post creation button click
    create_btn = site.find_element("xpath", create_button_xpath)
    create_btn.click()
    # input title
    title_input = site.find_element("xpath", title_xpath)
    title_input.send_keys(testdata["title"])
    # input description
    description_input = site.find_element("xpath", description_xpath)
    description_input.send_keys(testdata["description"])
    # input content
    content_input = site.find_element("xpath", content_xpath)
    content_input.send_keys(testdata["content"])
    # save post button click
    save_btn = site.find_element("xpath", save_button_xpath)
    save_btn.click()
    time.sleep(testdata["sleep_time"])
    # take title of created post by css
    created_post_title = site.find_element("css", created_post_title_css)
    assert created_post_title.text == testdata["title"]

# css_selector = "span.mdc-text-field__ripple"
# print(site.get_element_property("css", css_selector, "height"))
#
# xpath = '//*[@id="login"]/div[3]/button'
# print(site.get_element_property("xpath", xpath, "color"))
