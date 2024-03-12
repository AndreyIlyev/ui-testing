import allure
from selenium.webdriver.common.by import By
from base.base import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver

class GamePage(BaseObject):

    NUMBER_FIELD: tuple = (By.XPATH, '//*[@id="maxNumber"]')
    ATTEMPTS_FIELD: tuple = (By.ID, 'maxAttempts')
    GUESS_FIELD: tuple = (By.XPATH, '//*[@id="guess"]')
    START_BTN: tuple = (By.XPATH, '//*[@id="startBtn"]')
    CHECK_BTN: tuple = (By.XPATH, '//*[@id="playBtn"]')
    CONFIG_BTN: tuple = (By.XPATH, '//*[@id="backConfigBtn"]')
    ERROR_MSG: tuple = (By.XPATH, '//*[@id="errorConfigMessage"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Set max number')
    def set_max_number(self, value):
        self.send_keys(self.NUMBER_FIELD, value)

    @allure.step('Set max attempts')
    def set_max_attempts(self, value):
        self.send_keys(self.ATTEMPTS_FIELD, value)

    @allure.step('Start game')
    def start_game(self):
        self.click(self.START_BTN)

    @allure.step('Entering the guess')
    def set_guess(self, value):
        self.send_keys(self.GUESS_FIELD, value)

    @allure.step('Checking the result')
    def check_guess(self):
        self.click(self.CHECK_BTN)

    @allure.step('Back to config')
    def back_to_config(self):
        self.click(self.CONFIG_BTN)


