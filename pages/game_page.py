import allure
from selenium.webdriver.common.by import By
from base.base import BaseObject
from selenium.webdriver.remote.webdriver import WebDriver

class GamePage(BaseObject):

    NUMBER_FIELD: tuple = (By.XPATH, '//*[@id="maxNumber"]')
    ATTEMPTS_FIELD: tuple = (By.XPATH, '//*[@id="maxAttempts"]')
    GUESS_FIELD: tuple = (By.XPATH, '//*[@id="guess"]')
    START_BTN: tuple = (By.XPATH, '//*[@id="startBtn"]')
    CHECK_BTN: tuple = (By.XPATH, '//*[@id="playBtn"]')
    CONFIG_BTN: tuple = (By.XPATH, '//*[@id="backConfigBtn"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    @allure.step('Set value')
    def set_value(self, locator, value):
