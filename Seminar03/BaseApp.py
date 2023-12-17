from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, url):
        self.driver = driver
        self.base_url = url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator} ")

    def get_element_property(self, locator, el_property):
        element = self.find_element(locator)
        return element.value_of_css_property(el_property)

    def open_the_site(self):
        return self.driver.get(self.base_url)

    def get_alert_text(self):
        alert = self.driver.switch_to.alert
        return alert.text

