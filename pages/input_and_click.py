import allure
from selenium.webdriver.common.by import By
from base.base import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver
from support.assertions import Assertions


class InputAndClick(BaseObject, Assertions):
    TEXT_FIELD = (By.ID, 'inputText')
    ADD_BTN = (By.ID, 'addBtn')
    DELETE_BTN = (By.ID, 'deleteBtn')
    NOTE_DIV = (By.CSS_SELECTOR, '#items > div')
    text = 'test example'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Creating a new note')
    def enter_note(self):
        self.send_keys(self.TEXT_FIELD, self.text)
        self.click(self.ADD_BTN)

    def enter_note_check(self):
        self.enter_note()
        self.assert_equal(self.get_text(self.NOTE_DIV), self.text)

    @allure.step('Deleting the last note')
    def delete_note(self):
        self.click(self.DELETE_BTN)

    def delete_check(self):
        self.enter_note()
        self.delete_note()
        result = self._is_invisible(self.NOTE_DIV)
        self.assert_invisibility(result)
