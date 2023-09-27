import unittest
from unittest.mock import Mock
from ComputerGraphRectangles.input_validation import validate_input


class TestValidateInput(unittest.TestCase):
    def setUp(self):
        self.error_label = Mock()

    def test_validate_input_positive_integer(self):
        input_num = "42"
        result = validate_input(input_num, self.error_label)
        self.assertTrue(result)
        self.error_label.config.assert_called_once_with(text="")

    def test_validate_input_non_positive_integer(self):
        input_num = "-5"
        result = validate_input(input_num, self.error_label)
        self.assertFalse(result)
        self.error_label.config.assert_called_once_with(text="Введите целое положительное число больше 0")

    def test_validate_input_zero(self):
        input_num = "0"
        result = validate_input(input_num, self.error_label)
        self.assertFalse(result)
        self.error_label.config.assert_called_once_with(text="Введите целое положительное число больше 0")

    def test_validate_input_letters(self):
        input_num = "abc"
        result = validate_input(input_num, self.error_label)
        self.assertFalse(result)
        self.error_label.config.assert_called_once_with(text="Введите числовое значение")

    def test_validate_input(self):
        input_num = "@!&^%"
        result = validate_input(input_num, self.error_label)
        self.assertFalse(result)
        self.error_label.config.assert_called_once_with(text="Введите числовое значение")

if __name__ == "__main__":
    unittest.main()