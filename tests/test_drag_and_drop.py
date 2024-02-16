import pytest
from support.assertions import Assertions

def test_drag_and_drop(drag_and_drop_page):
    drag_and_drop_page.order_word()