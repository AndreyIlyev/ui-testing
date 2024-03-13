import allure
import random
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
    START_GAME_MSG: tuple = (By.XPATH, "//span[contains(text(),'Rules')]")
    RESULT_MSG: tuple = (By.XPATH, '//*[@id="resultMessage"]')
    CONFIG_MSG: tuple = (By.XPATH, "//span[contains(text(), 'Configuration:')]")

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
    def set_guess(self, value):
        self.send_keys(self.GUESS_FIELD, value)

    @allure.step('Checking the result')
    def check_guess(self):
        self.click(self.CHECK_BTN)

    @allure.step('Back to config')
    def back_to_config(self):
        self.click(self.CONFIG_BTN)

    def test_game(self):
        self.set_max_number(random.randint(10, 20))
        self.set_max_attempts(random.randint(1, 9))
        self.start_game_btn()
        with allure.step('Checking the game started'):
            assert self._is_visible(self.START_GAME_MSG)
        self.send_keys(self.GUESS_FIELD, str(random.randint(10, 20)))
        self.check_guess()
        with allure.step('Checking the result message is  visible'):
            assert self._is_visible(self.RESULT_MSG)
        with allure.step('Checking "Back to comfig" button is working '):
            self.back_to_config()
            assert self._is_visible(self.CONFIG_MSG)






    # def test_gaming(self):
    #     self.set_max_number(random.randint(10, 20))
    #     self.set_max_attempts(random.randint(1, 9))
    #     self.start_game_btn()
    #     self.send_keys(self.GUESS_FIELD, str(random.randint(10,20)))
    #     self.check_guess()
    #     assert self._is_visible(self.RESULT_MSG)
    #
    # def test_back_to_config(self):
    #     self.set_max_number(random.randint(10, 20))
    #     self.set_max_attempts(random.randint(1, 9))
    #     self.start_game_btn()
    #     self.send_keys(self.GUESS_FIELD, str(random.randint(10, 20)))
    #     self.check_guess()
    #     self.back_to_config()
    #     assert self._is_visible(self.CONFIG_MSG)
