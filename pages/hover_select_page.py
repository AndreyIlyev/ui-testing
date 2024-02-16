from selenium.webdriver.common.by import By
from base.base import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions


class HoverSelectPage(BaseObject, Assertions ):

    SELECT_BTN: tuple = (By.CLASS_NAME, 'dropdown')
    LIST_ITEM : tuple = (By.XPATH, '/html/body/div[2]/div/div[2]/ul/li[2]/a')
    LINK : str = 'https://toghrulmirzayev.github.io/ui-simulator/input-and-click.html'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open_list(self):
        self.hover(self.SELECT_BTN)
        assert self._is_visible(self.LIST_ITEM)



    def select_item(self,):
        self.open_list()
        self.click(self.LIST_ITEM)
        self.assert_equal(self.get_current_url(), self.LINK)




