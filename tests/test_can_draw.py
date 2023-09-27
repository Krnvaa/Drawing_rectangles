import unittest
from unittest.mock import Mock, patch
from ComputerGraphRectangles.main import DrawingRectangles

class TestCanDrawRectangle(unittest.TestCase):
    @patch('ComputerGraphRectangles.main.tk.Tk')
    def setUp(self, mock_tk):
        self.root = mock_tk()
        self.app = DrawingRectangles(self.root)

    def tearDown(self):
        self.root.destroy()

    def test_can_draw_rectangle_with_valid_values(self):
        self.app.min_size = Mock()
        self.app.min_size.return_value = 0
        x = 10
        y = 20
        result = self.app.can_draw_rectangle(x, y)
        self.assertTrue(result)

    def test_can_draw_rectangle_with_zero_values(self):
        self.app.min_size = Mock()
        self.app.min_size.return_value = 0
        x = 0
        y = 20
        result = self.app.can_draw_rectangle(x, y)
        self.assertFalse(result)

    def test_can_draw_rectangle_with_negative_values(self):
        self.app.min_size = Mock()
        self.app.min_size.return_value = 0
        x = -10
        y = 20
        result = self.app.can_draw_rectangle(x, y)
        self.assertFalse(result)

if __name__ == "main":
    unittest.main()