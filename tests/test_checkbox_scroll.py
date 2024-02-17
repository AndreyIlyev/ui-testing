import allure
import pytest


@allure.title('Test of scrolling and selecting')
def test_checkboxes(checkbox_scroll_page):
    checkbox_scroll_page.mark_boxes()
