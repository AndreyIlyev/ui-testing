import allure
import random
from selenium.webdriver.common.by import By
from base.base import BaseObject
from support.assertions import Assertions
from selenium.webdriver.remote.webdriver import WebDriver


class GamePage(BaseObject, Assertions):
    NUMBER_FIELD: tuple = (By.XPATH, '//*[@id="maxNumber"]')
    ATTEMPTS_FIELD: tuple = (By.ID, 'maxAttempts')
    GUESS_FIELD: tuple = (By.XPATH, '//*[@id="guess"]')
    START_BTN: tuple = (By.XPATH, '//*[@id="startBtn"]')
    CHECK_BTN: tuple = (By.XPATH, '//*[@id="playBtn"]')
    CONFIG_BTN: tuple = (By.XPATH, '//*[@id="backConfigBtn"]')
    ERROR_MSG: tuple = (By.XPATH, '//*[@id="errorConfigMessage"]')
    INFORM_MSG: tuple = (By.XPATH, '/html/body/div[2]/h3')
    RESULT_MSG: tuple = (By.XPATH, '//*[@id="resultMessage"]')
    CONFIG_MSG = 'Configuration: Max number and max attempt should be more than 0 and can\'t be empty'
    RULES_MSG = 'Rules: Secret number is hidden. Guess it.'
    __attempts = 0

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Set max number')
    def set_max_number(self, value):
        self.send_keys(self.NUMBER_FIELD, value)

    @allure.step('Set max attempts')
    def set_max_attempts(self, value):
        self.send_keys(self.ATTEMPTS_FIELD, value)

    @allure.step('Start game')
    def start_game_btn(self):
        self.click(self.START_BTN)

    @allure.step('Entering the guess')
    def set_guess(self):
        self.send_keys(self.GUESS_FIELD, str(random.randint(0, 10)))

    @allure.step('Checking the result')
    def check_guess(self):
        self.click(self.CHECK_BTN)

    @allure.step('Back to config')
    def to_config(self):
        self.click(self.CONFIG_BTN)

    def start_game(self):
        number = random.randint(0, 10)
        self.__attempts = random.randint(3, 6)
        self.set_max_number(number)
        self.set_max_attempts(self.__attempts)
        self.start_game_btn()

    def attempt_guess(self):
        self.start_game()
        for i in range(self.__attempts):
            self.set_guess()
            self.check_guess()
            msg = self.get_text(self.RESULT_MSG)
            if msg.startswith('Congratulations!'):
                break
            else:
                self._is_visible(self.GUESS_FIELD).clear()
                continue

    def back_to_start(self):
        self.attempt_guess()
        self.to_config()
