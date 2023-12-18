import logging

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, time=10):
        try:
            element = WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator} ")
        except:
            logging.exception("Find element exception")
            element = None
        return element

    def get_element_property(self, locator, el_property):
        element = self.find_element(locator)
        if element:
           return element.value_of_css_property(el_property)
        else:
            logging.exception(f"Property {el_property} not found in element with locator {locator}")
            return None

    def open_the_site(self):
        try:
            start_browsing = self.driver.get(self.base_url)
        except:
            logging.exception("Exception while open the site")
            start_browsing = None
        return start_browsing

    def get_alert_text(self):
        try:
            alert = self.driver.switch_to.alert
            return alert.text
        except:
            logging.exception("Exception with alert")
            return None
