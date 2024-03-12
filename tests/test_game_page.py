import allure

@allure.title('Testing running game')
def test_running_game(game_page):
    game_page.set_max_number(15)
    game_page.set_max_attempts(3)
    game_page.start_game()
