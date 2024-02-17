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
        with allure.step('Entering text into field'):
            self.send_keys(self.TEXT_FIELD, self.text)
        with allure.step('Click add button'):
            self.click(self.ADD_BTN)

    @allure.step('Checking creating a new note')
    def enter_note_check(self):
        self.enter_note()
        with allure.step('Checking the note was created'):
            self.assert_equal(self.get_text(self.NOTE_DIV), self.text)

    @allure.step('Deleting the last note')
    def delete_note(self):
        with allure.step('Click delete button'):
            self.click(self.DELETE_BTN)

    @allure.step('Checking the note was deleted ')
    def delete_check(self):
        self.enter_note()
        self.delete_note()
        with allure.step('Assertion of deleting the note'):
            result = self._is_invisible(self.NOTE_DIV)
            self.assert_invisibility(result)
