import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.index_page import IndexPage
from pages.hover_select_page import HoverSelectPage
from env_config import ConfigURL
from pages.input_and_click import InputAndClick
from pages.drag_and_drop_page import DragAndDrop
from pages.check_validate_page import CheckValidate
from pages.checkbox_scroll import CheckboxScroll


@pytest.fixture
def get_chrome_options():
    options = ChromeOptions()
    return options


@pytest.fixture
def get_webdriver(get_chrome_options):
    driver = webdriver.Chrome(options=get_chrome_options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture
def index_page(get_webdriver):
    get_webdriver.get(ConfigURL.BASE_URL)
    yield IndexPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture
def hover_select_page(get_webdriver):
    get_webdriver.get(ConfigURL.HOVER_URL)
    yield HoverSelectPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture
def input_and_click_page(get_webdriver):
    get_webdriver.get(ConfigURL.INPUT_URL)
    yield InputAndClick(get_webdriver)
    get_webdriver.quit()

@pytest.fixture
def drag_and_drop_page(get_webdriver):
    get_webdriver.get(ConfigURL.DRAG_URL)
    yield DragAndDrop(get_webdriver)
    get_webdriver.quit()

@pytest.fixture
def check_validate_page(get_webdriver):
    get_webdriver.get(ConfigURL.CHECK_URL)
    yield CheckValidate(get_webdriver)
    get_webdriver.quit()

@pytest.fixture
def checkbox_scroll_page(get_webdriver):
    get_webdriver.get(ConfigURL.CHECKBOX_URL)
    yield CheckboxScroll(get_webdriver)
    get_webdriver.quit()