import allure
from selenium.webdriver.common.by import By
from base.base import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions


class CheckboxScroll(BaseObject, Assertions):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    CHECKBOX = (By.XPATH, '/html/body/div[2]/ul/li[15]/input')
    COUNTER = (By.XPATH, '//*[@id="counter"]')

    @allure.step('Selecting checkbox')
    def mark_boxes(self):
        with allure.step('Scrolling to checkbox'):
            self.scroll_to(self.CHECKBOX)
        with allure.step('Selecting checkbox'):
            self.click(self.CHECKBOX)
        with allure.step('Checking counter of selected checkboxes'):
            expected = '1'
            actual = self._is_visible(self.COUNTER).text
            self.assert_equal(actual, expected)
