import pytest
import allure
from env_config import Creds
from env_config import ConfigURL

@allure.description('Success login')
@allure.label('owner', 'Andrey')
@allure.title('Successful login')
@allure.suite('Authorization suite')
@allure.severity(allure.severity_level.BLOCKER)
def test_successful_login(index_page):
    index_page.enter_username()
    index_page.enter_password()
    index_page.click_login_btn()
    index_page.validate_url(url=ConfigURL.AUTH_URL)


@pytest.mark.parametrize(
    'login, password', [
        (Creds.TEST_USERNAME, 'incorrect_password'),
        ('incorrect_username', Creds.TEST_PASSWORD),
        ('incorrect_username', 'incorrect_password')
    ]
                         )
@allure.description('Invalid authorization with different values')
@allure.suite('Authorization suite')
@allure.title('invalid credentials')
def test_invalid_creds(index_page, login, password):
    index_page.enter_username(login)
    index_page.enter_password(password)
    index_page.click_login_btn()
    index_page.validate_msg('Password or username is incorrect')


