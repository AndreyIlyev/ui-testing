import allure
import pytest


@allure.title('Checking drop list is visible')
def test_droplist(hover_select_page):
    hover_select_page.open_list()


@allure.title('Selecting item from  drop list')
def test_select_item(hover_select_page):
    hover_select_page.select_item()
