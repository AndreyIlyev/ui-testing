import allure
import random

import pytest


@allure.title('Testing the game process')
def test_game(game_page):
    game_page.test_game()


case_1 = ['', 3, 'Please enter valid configurations']
case_2 = [5, '', 'Please enter valid configurations']
case_3 = ['51', 'f', 'Please enter valid configurations']
case_4 = ['', '', 'Please enter valid configurations']
case_5 = [-6, 3, 'Please enter valid configurations']


@pytest.mark.parametrize('number, attempts, expected_msg', (case_1, case_2, case_3, case_4, case_5))
def test_negative_values(game_page, number, attempts, expected_msg):
    game_page.set_max_number(number)
    game_page.set_max_attempts(attempts)
    game_page.start_game_btn()
    actual_msg = game_page.get_text(game_page.ERROR_MSG)
    assert actual_msg == expected_msg
