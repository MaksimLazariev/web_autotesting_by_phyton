import logging
from selenium.webdriver.common.by import By
from BaseApp import BasePage


class TestSearchLocators:
    LOCATOR_LOGIN_FIELD = (
        By.XPATH,
        """//*[@id="login"]/div[1]/label/input""")  # Локатор поля Логин
    LOCATOR_PASSWORD_FIELD = (
        By.XPATH,
        """//*[@id="login"]/div[2]/label/input""")  # Локатор поля Пароль
    LOCATOR_LOGIN_BTN = (
        By.XPATH, """//*[@id="login"]/div[3]/button""")  # Локатор кнопки Логин
    LOCATOR_ERROR_FIELD = (By.XPATH,
                           """//*[@id="app"]/main/div/div/div[2]/h2""")  # Локатор поля ошибки
    LOCATOR_RESULT_FIELD = (
        By.XPATH,
        """//*[@id="app"]/main/nav/a/span""")  # Локатор заголовка Home

    LOCATOR_CREATE_BLOG_BTN = (By.XPATH, """//*[@id="create-btn"]""")
    LOCATOR_TITLE_FIELD = (
        By.XPATH, """//*[@id="create-item"]/div/div/div[1]/div/label/input""")
    LOCATOR_DESCRIPTION_FIELD = (By.XPATH,
                                 """//*[@id="create-item"]/div/div/div[2]/div/label/span/textarea""")
    LOCATOR_CONTENT_FIELD = (By.XPATH,
                             """//*[@id="create-item"]/div/div/div[3]/div/label/span/textarea""")
    LOCATOR_SAVE_BLOG_BTN = (
        By.XPATH, """//*[@id="create-item"]/div/div/div[7]/div/button""")
    LOCATOR_CREATED_BLOG_TITLE = (By.CSS_SELECTOR, """h1""")

    LOCATOR_CONTACT_US_BTN = (
        By.XPATH, """//*[@id="app"]/main/nav/ul/li[2]/a""")
    LOCATOR_CONTACT_NAME_FIELD = (
        By.XPATH, """//*[@id="contact"]/div[1]/label/input""")
    LOCATOR_CONTACT_EMAIL_FIELD = (
        By.XPATH, """//*[@id="contact"]/div[2]/label/input""")
    LOCATOR_CONTACT_CONTENT_FIELD = (
        By.XPATH, """//*[@id="contact"]/div[3]/label/span/textarea""")
    LOCATOR_CONTACT_SEND_BTN = (
        By.XPATH, """//*[@id="contact"]/div[4]/button""")


class OperationsHelper(BasePage):
    # функция ввода логина
    def enter_login(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_LOGIN_FIELD[1]}")
        log_field = self.find_element(TestSearchLocators.LOCATOR_LOGIN_FIELD)
        log_field.clear()
        log_field.send_keys(word)

    # функция ввода пароля
    def enter_password(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_PASSWORD_FIELD[1]}")
        password_field = self.find_element(TestSearchLocators.LOCATOR_PASSWORD_FIELD)
        password_field.clear()
        password_field.send_keys(word)

    # функция нажатия кнопки login
    def click_login_button(self):
        logging.info(f"Click login button")
        self.find_element(TestSearchLocators.LOCATOR_LOGIN_BTN).click()

    # функция вывода текста (в нашем случае 401)
    def get_error_text(self):
        error_field = self.find_element(TestSearchLocators.LOCATOR_ERROR_FIELD, time=2)
        error_text = error_field.text
        logging.info(f"We find text {error_text} in error field {TestSearchLocators.LOCATOR_ERROR_FIELD[1]}")
        return error_text

    def get_login_text(self):
        text_field = self.find_element(TestSearchLocators.LOCATOR_RESULT_FIELD, time=2)
        blog_text = text_field.text
        logging.info(f"We find text {blog_text} in error field {TestSearchLocators.LOCATOR_RESULT_FIELD[1]}")
        return  blog_text

    def click_create_post_button(self):
        logging.info(f"Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_CREATE_BLOG_BTN).click()

    def enter_post_title(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_TITLE_FIELD[1]}")
        tittle_field = self.find_element(TestSearchLocators.LOCATOR_TITLE_FIELD)
        tittle_field.clear()
        tittle_field.send_keys(word)

    def enter_post_description(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_DESCRIPTION_FIELD[1]}")
        description_field = self.find_element(TestSearchLocators.LOCATOR_DESCRIPTION_FIELD)
        description_field.clear()
        description_field.send_keys(word)

    def enter_post_content(self, word):
        logging.info(f"Send {word} to element {TestSearchLocators.LOCATOR_CONTENT_FIELD[1]}")
        content_field = self.find_element(TestSearchLocators.LOCATOR_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def click_save_post_button(self):
        logging.info(f"Click new post button")
        self.find_element(TestSearchLocators.LOCATOR_SAVE_BLOG_BTN).click()

    def get_new_post_text(self):
        post_field = self.find_element(TestSearchLocators.LOCATOR_CREATED_BLOG_TITLE, time=2)
        text = post_field.text
        logging.info(f"We find text {text} in error field {TestSearchLocators.LOCATOR_CREATED_BLOG_TITLE[1]}")
        return text

    def click_contact_us_button(self):
        logging.info(f"Click contact us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_US_BTN).click()

    def enter_feedback_name(self, word):
        logging.info(
            f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD[1]}")
        content_field = self.find_element(
            TestSearchLocators.LOCATOR_CONTACT_NAME_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def enter_feedback_email(self, word):
        logging.info(
            f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD[1]}")
        content_field = self.find_element(
            TestSearchLocators.LOCATOR_CONTACT_EMAIL_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def enter_feedback_content(self, word):
        logging.info(
            f"Send {word} to element {TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD[1]}")
        content_field = self.find_element(
            TestSearchLocators.LOCATOR_CONTACT_CONTENT_FIELD)
        content_field.clear()
        content_field.send_keys(word)

    def click_feedback_sent_button(self):
        logging.info(f"Click send contact us button")
        self.find_element(TestSearchLocators.LOCATOR_CONTACT_SEND_BTN).click()

    def get_alert(self):
        logging.info("Get alert text")
        alert_text = self.get_alert_text()
        logging.info(alert_text)
        return alert_text



