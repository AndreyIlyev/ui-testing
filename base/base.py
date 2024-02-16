from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.common.action_chains import ActionChains
from support.logger import log_func
from selenium.common import TimeoutException


class BaseObject:
    LOG = log_func()

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def _is_visible(self, locator: tuple) -> WebElement:
        try:
            result = self.wait.until(ec.visibility_of_element_located(locator))
            self.LOG.info(f'Element {locator} is {result}')
            return result
        except TimeoutException:
            self.LOG.error(f'Element {locator} is invisible')

    def _is_invisible(self, locator: tuple) -> WebElement:
        try:
            result = self.wait.until(ec.invisibility_of_element_located(locator))
            self.LOG.info(f'Element {locator} is {result}')
            return result

        except AssertionError:
            self.LOG.error(f'Element {locator} is visible')

    def _is_clickable(self, locator: tuple) -> WebElement:
        try:
            result = self.wait.until(ec.element_to_be_clickable(locator))
            self.LOG.info(f'Element{locator} is clickable')
            return result
        except BaseException:
            self.LOG.error(f'Element{locator} is not clickable')


    def click(self, locator: tuple):
        self._is_clickable(locator).click()

    def send_keys(self, locator: tuple, value: str):
        self._is_visible(locator).send_keys(value)

    def get_text(self, locator) -> str:
        try:
            result = self._is_visible(locator).text
            self.LOG.info(f'Text from element {locator} is {result}')
            return result
        except BaseException:
            self.LOG.error(f'Text from element{locator} has not received')



    def get_current_url(self) -> str:
        result = self.driver.current_url
        self.LOG.info(f'Current url is {result}')
        return result

    def hover(self, locator: tuple):
        try:
            mouse = ActionChains(self.driver)
            element = self._is_visible(locator)
            mouse.move_to_element(element).perform()
            self.LOG.info(f'Cursor hovered over element {element}')
        except BaseException:
            self.LOG.error(f'Cursor does not hovered over element {locator}')

    def scroll_to(self, locator: tuple):
        try:
            actions = ActionChains(self.driver)
            element = self._is_visible(locator)
            actions.move_to_element(element).perform()
            self.LOG.info(f'Scroll to element {locator} was performed')
        except BaseException:
            self.LOG.error(f'Scroll to element {locator} was not performed')

    def drag_and_drop(self, to_drag: tuple, to_drop: tuple):
        try:
            actions = ActionChains(self.driver)
            actions.drag_and_drop(self._is_clickable(to_drag), self._is_visible(to_drop)).perform()
            self.LOG.error(f'Element {to_drag} dragged, and dropped to {to_drop}')
        except BaseException:
            self.LOG.error(f'Actions was not performed')
