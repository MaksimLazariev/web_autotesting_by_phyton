import logging
import yaml
from selenium.webdriver.common.by import By
from BaseApp import BasePage


class TestSearchLocators:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])


class OperationsHelper(BasePage):
    # Метод ввода текста в поле ввода
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")

        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

    # Метод клика кнопки
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
        logging.debug(f"Clicked {element_name} button")
        return True

    # Метод получения текста от элемента
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text

    # МЕТОДЫ ВВОДА ТЕКСТА
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_LOGIN_FIELD"],
                                   word, description="login form")

    def enter_password(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_PASSWORD_FIELD"],
                                   word, description="password form")

    def enter_post_title(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_TITLE_FIELD"],
                                   word, description="title form")

    def enter_post_description(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_DESCRIPTION_FIELD"],
            word, description="description form")

    def enter_post_content(self, word):
        self.enter_text_into_field(TestSearchLocators.ids["LOCATOR_CONTENT_FIELD"],
                                   word, description="content form")

    def enter_feedback_name(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_CONTACT_NAME_FIELD"],
            word, description="contact name form")

    def enter_feedback_email(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_CONTACT_EMAIL_FIELD"],
            word, description="contact email form")

    def enter_feedback_content(self, word):
        self.enter_text_into_field(
            TestSearchLocators.ids["LOCATOR_CONTACT_CONTENT_FIELD"],
            word, description="contact content form")

    # МЕТОДЫ КЛИКА
    def click_login_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_LOGIN_BTN"],
                          description="login")

    def click_create_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CREATE_BLOG_BTN"],
                          description="create blog")

    def click_save_post_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_SAVE_BLOG_BTN"],
                          description="save blog")

    def click_contact_us_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_US_BTN"],
                          description="contact us create")

    def click_feedback_sent_button(self):
        self.click_button(TestSearchLocators.ids["LOCATOR_CONTACT_SEND_BTN"],
                          description="contact us send")

    # МЕТОДЫ ПОЛУЧЕНИЯ ТЕКСТА
    def get_error_text(self):
        return self.get_text_from_element(
            TestSearchLocators.ids["LOCATOR_ERROR_FIELD"])

    def get_login_text(self):
        return self.get_text_from_element(
            TestSearchLocators.ids["LOCATOR_RESULT_FIELD"])

    def get_new_post_text(self):
        return self.get_text_from_element(
            TestSearchLocators.ids["LOCATOR_CREATED_BLOG_TITLE"])

    def get_alert(self):
        logging.debug("Get alert text")
        alert_text = self.get_alert_text()
        logging.debug(alert_text)
        return alert_text
