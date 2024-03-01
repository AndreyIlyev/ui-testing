пшimport pytest
import allure


@allure.title('Adding a new text note')
def test_add_note(input_and_click_page):
    input_and_click_page.enter_note_check()


@allure.title('Removing the last text note')
def test_remove_note(input_and_click_page):
    input_and_click_page.delete_check()
