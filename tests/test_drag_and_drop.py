import allure


@allure.title('Testing drag and drop function')
def test_drag_and_drop(drag_and_drop_page):
    drag_and_drop_page.order_word()
