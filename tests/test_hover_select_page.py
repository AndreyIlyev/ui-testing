import pytest


def test_droplist(hover_select_page):
    hover_select_page.open_list()


def test_select_item(hover_select_page):
    hover_select_page.select_item()

