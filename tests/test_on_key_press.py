import unittest
from unittest.mock import Mock, patch
from ComputerGraphRectangles.main import DrawingRectangles

class TestOnKeyPress(unittest.TestCase):
    @patch('ComputerGraphRectangles.main.tk.Tk')
    def setUp(self, mock_tk):
        self.root = mock_tk()
        self.canvas = Mock()
        self.error_label = Mock()
        self.app = DrawingRectangles(self.root)
        self.app.canvas = self.canvas
        self.app.error_label = self.error_label

    def tearDown(self):
        self.root.destroy()

    def test_on_key_press_return_key(self):
        event = Mock(keysym="Return")
        self.app.draw_rectangle = Mock()
        self.app.on_key_press(event)
        self.app.draw_rectangle.assert_called_once()

    def test_on_key_press_d_key(self):
        event = Mock(keysym="d")
        self.app.delete_rectangle = Mock()
        self.app.on_key_press(event)
        self.app.delete_rectangle.assert_called_once()

    def test_on_key_press_escape_key(self):
        event = Mock(keysym="Escape")
        self.root.destroy = Mock()
        self.app.on_key_press(event)
        self.root.destroy.assert_called_once()

if __name__ == "main":
    unittest.main()