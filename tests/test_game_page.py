import allure
import random


@allure.title('Testing the game process')
def test_game(game_page):
    # game_page.set_max_number(random.randint(10, 20))
    # game_page.set_max_attempts(random.randint(10, 20))
    # game_page.start_game_btn()
    # assert game_page._is_visible(game_page.START_GAME_MSG)
    game_page.test_game()
