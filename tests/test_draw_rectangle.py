import unittest
from unittest.mock import Mock, patch
import tkinter as tk
from ComputerGraphRectangles.main import DrawingRectangles

class TestDrawRectangle(unittest.TestCase):
    @patch('ComputerGraphRectangles.main.tk.Tk')
    def setUp(self, mock_tk):
        self.root = mock_tk()
        self.canvas = Mock()
        self.error_label = Mock()
        self.hx_entry = Mock()
        self.hy_entry = Mock()
        self.app = DrawingRectangles(self.root)
        self.app.canvas = self.canvas
        self.app.error_label = self.error_label
        self.app.hx_entry = self.hx_entry
        self.app.hy_entry = self.hy_entry
        self.app.rectangles = []
        self.app.x = None
        self.app.y = None
        self.app.hx_increment = None
        self.app.hy_increment = None
        self.app.last_deleted_x = None
        self.app.last_deleted_y = None

    def tearDown(self):
        self.root.destroy()

    def test_draw_rectangle_with_valid_values(self):
        self.app.x = 200
        self.app.y = 300
        self.hx_entry.get.return_value = "10"
        self.hy_entry.get.return_value = "5"
        self.app.can_draw_rectangle = Mock(return_value=True)
        self.app.draw_rectangle()
        self.assertEqual(len(self.app.rectangles), 1)

    def test_draw_rectangle_with_invalid_values(self):
        self.app.x = 10
        self.app.y = 10
        self.hx_entry.get.return_value = "10"
        self.hy_entry.get.return_value = "5"
        self.app.can_draw_rectangle = Mock(return_value=False)
        self.app.draw_rectangle()
        self.canvas.create_rectangle.assert_not_called()
        self.error_label.config.assert_called_once_with(text="Прямоугольник еще меньше построить уже нельзя")

    def test_compute_rectangle_coordinates(self):
        self.app.x = 500
        self.app.y = 500
        self.app.hx_entry.get.return_value = "10"
        self.app.hy_entry.get.return_value = "5"
        expected_x1 = (self.app.width_canvas - self.app.x) / 2
        expected_y1 = (self.app.height_canvas - self.app.y) / 2
        expected_x2 = expected_x1 + self.app.x
        expected_y2 = expected_y1 + self.app.y
        self.app.draw_rectangle()
        # Проверяем, что create_rectangle вызывается с правильными координатами
        self.app.canvas.create_rectangle.assert_called_once_with(
            expected_x1, expected_y1,
            expected_x2, expected_y2
        )

if __name__ == "__main__":
    unittest.main()