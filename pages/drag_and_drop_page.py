from selenium.webdriver.common.by import By
from base.base import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions

class DragAndDrop(BaseObject, Assertions):
    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    ITEM_1 = (By.ID, 'item-1')
    ITEM_2 = (By.ID, 'item-2')
    ITEM_3 = (By.ID, 'item-3')
    ITEM_4 = (By.ID, 'item-4')
    ITEM_5 = (By.ID, 'item-5')
    ITEM_6 = (By.ID, 'item-6')
    ITEM_7 = (By.ID, 'item-7')
    DONE_BTN = (By.CLASS_NAME, 'done')

    def order_word(self):
        self.drag_and_drop(self.ITEM_3,self.ITEM_1)
        self.drag_and_drop(self.ITEM_2, self.ITEM_1)
        self.drag_and_drop(self.ITEM_7, self.ITEM_1)
        self.drag_and_drop(self.ITEM_4, self.ITEM_1)
        self.drag_and_drop(self.ITEM_5, self.ITEM_6)
        assert self._is_visible(self.DONE_BTN)