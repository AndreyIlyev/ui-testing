import pytest


@pytest.mark.parametrize('value, error_msg',
                         [
                             ('15', 'Valid'),
                             ('9', 'Not in range'),
                             ('51', 'Not in range'),
                             ('-1', 'Negative integer')

                         ])
def test_check_values(check_validate_page, value, error_msg):
    check_validate_page.enter_value(value)
    actual_msg = check_validate_page.get_text(check_validate_page.VALID_SQUARE)
    check_validate_page.assert_equal(actual_msg, error_msg)
