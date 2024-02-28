from dotenv import load_dotenv
import os


class Creds:
    load_dotenv()

    TEST_USERNAME = os.getenv("TEST_USERNAME")
    TEST_PASSWORD = os.getenv("TEST_PASSWORD")


class ConfigURL:
    BASE_URL = 'https://toghrulmirzayev.github.io/ui-simulator/'
    HOVER_URL = f'{BASE_URL}hover_and_select.html'
    INPUT_URL = f'{BASE_URL}input-and-click.html'
    DRAG_URL = f'{BASE_URL}drag-and-drop.html'
    CHECK_URL = f'{BASE_URL}check_and_validate.html'
    CHECKBOX_URL = f'{BASE_URL}checkbox-and-scroll.html'
