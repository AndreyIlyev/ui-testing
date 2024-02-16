from base.base import BaseObject
from support.assertions import Assertions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By


class CheckValidate(BaseObject, Assertions):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    INPUT_FIELD = (By.ID, 'dataInput')
    VALID_SQUARE = (By.ID, 'validationSquare')

    def enter_value(self, value: str = ''):
        self.send_keys(self.INPUT_FIELD, value)
