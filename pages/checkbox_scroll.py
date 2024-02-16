from selenium.webdriver.common.by import By
from base.base import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions


class CheckboxScroll(BaseObject, Assertions):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    CHECKBOX = (By.XPATH, '/html/body/div[2]/ul/li[15]/input')
    COUNTER = (By.ID, '#counter')

    def mark_boxes(self):
        self.scroll_to(self.CHECKBOX)
        self.click(self.CHECKBOX)
        expected = 1
        actual = self._is_visible(self.COUNTER)
        self.assert_equal(actual, expected)
