import allure
from selenium.webdriver.common.by import By
from base.base import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions


class HoverSelectPage(BaseObject, Assertions):
    SELECT_BTN: tuple = (By.CLASS_NAME, 'dropdown')
    LIST_ITEM: tuple = (By.XPATH, '/html/body/div[2]/div/div[2]/ul/li[2]/a')
    LINK: str = 'https://toghrulmirzayev.github.io/ui-simulator/input-and-click.html'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Open drop list')
    def open_list(self):
        with allure.step('Hovering curson over the select button'):
            self.hover(self.SELECT_BTN)
        with allure.step('Checking the drop list is visible'):
            self.assert_visibility(self._is_visible(self.LIST_ITEM))
    @allure.step('Selecting item from the drop list')
    def select_item(self):
        self.open_list()
        self.click(self.LIST_ITEM)
        with allure.step('Checking the item leads to new page'):
            self.assert_equal(self.get_current_url(), self.LINK)
