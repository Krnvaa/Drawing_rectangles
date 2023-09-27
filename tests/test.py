import unittest
from unittest.mock import Mock, patch
from ComputerGraphRectangles.main import DrawingRectangles

class TestDeleteRectangle(unittest.TestCase):
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

    def test_delete_rectangle_with_rectangles(self):
        # Проверяем удаление прямоугольника при наличии прямоугольников на холсте
        rectangle_mock = Mock()
        self.app.rectangles = [rectangle_mock]
        self.canvas.coords.return_value = (0, 0, 10, 10)
        self.app.delete_rectangle()
        self.assertEqual(len(self.app.rectangles), 0)
        self.assertEqual(self.app.last_deleted_x, 10)
        self.assertEqual(self.app.last_deleted_y, 10)
        self.error_label.config.assert_called_once_with(text="")

    def test_delete_rectangle_without_rectangles(self):
        # Проверяем удаление прямоуголька при отсутствии прямоугольников на холсте
        self.app.rectangles = []
        self.app.delete_rectangle()
        self.assertEqual(self.app.last_deleted_x, None)
        self.assertEqual(self.app.last_deleted_y, None)
        self.error_label.config.assert_not_called()

if __name__ == "__main__":
    unittest.main()