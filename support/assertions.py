from support.error_messages import AssertionsMessages


class Assertions:
    @staticmethod
    def assert_equal(actual, expected):
        assert actual == expected, AssertionsMessages.ASSERT_EQUAL.format(expected, actual)

    @staticmethod
    def assert_visibility(element):
        assert element

    @staticmethod
    def assert_invisibility(element):
        assert element
