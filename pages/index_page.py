from selenium.webdriver.common.by import By
from base.base import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions
import allure


class IndexPage(BaseObject, Assertions):
    USERNAME_FIELD: tuple = (By.ID, "username")
    PASSWORD_FIELD: tuple = (By.ID, "password")
    LOGIN_BTN: tuple = (By.CLASS_NAME, "login-button")
    ERROR_MSG: tuple = (By.CLASS_NAME, 'error-message')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Entering user name')
    def enter_username(self, username='correct_username'):
        self.send_keys(self.USERNAME_FIELD, username)

    @allure.step('Entering password')
    def enter_password(self, password='correct_password'):
        self.send_keys(self.PASSWORD_FIELD, password)

    @allure.step('Click login button')
    def click_login_btn(self):
        self.click(self.LOGIN_BTN)

    @allure.step('Validation of url')
    def validate_url(self, url):
        with allure.step('Checking the authorization is done '):
            self.assert_equal(actual=self.get_current_url(),
                              expected=url)

    @allure.step('Checking error message is visible')
    def validate_msg(self, error_msg):
        self.assert_equal(actual=self.get_text(self.ERROR_MSG), expected=error_msg)
