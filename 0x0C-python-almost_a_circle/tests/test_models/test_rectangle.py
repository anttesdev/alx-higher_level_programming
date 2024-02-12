#!/usr/bin/python3
"""
A rectangle testing unitest module
"""


import unittest
from unittest.mock import patch
from io import StringIO
from models.rectangle import Rectangle


class TestRectangleInitialization(unittest.TestCase):
    def test_valid_initialization(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(rectangle.width, 5)
        self.assertEqual(rectangle.height, 10)
        self.assertEqual(rectangle.x, 2)
        self.assertEqual(rectangle.y, 3)
        self.assertEqual(rectangle.id, 1)

    def test_invalid_width(self):
        with self.assertRaises(ValueError):
            Rectangle(-5, 10, 2, 3, 1)

    def test_invalid_height(self):
        with self.assertRaises(ValueError):
            Rectangle(5, -10, 2, 3, 1)

    def test_invalid_x(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, -2, 3, 1)

    def test_invalid_y(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3, 1)

    def test_invalid_id(self):
        with self.assertRaises(ValueError):
            Rectangle(5, 10, 2, -3, 1)

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            Rectangle("invalid", 10, 2, 3, 1)

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            Rectangle(5, "invalid", 2, 3, 1)

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, "invalid", 3, 1)

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Rectangle(5, 10, 2, "invalid", 1)

class TestRectangleWidthProperty(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_valid_width_setter(self):
        self.rectangle.width = 8
        self.assertEqual(self.rectangle.width, 8)

    def test_invalid_width_negative(self):
        with self.assertRaises(ValueError):
            self.rectangle.width = -5

    def test_invalid_width_type(self):
        with self.assertRaises(TypeError):
            self.rectangle.width = "invalid"

    def test_width_zero(self):
        with self.assertRaises(ValueError):
            self.rectangle.width = 0

    def test_width_float(self):
        with self.assertRaises(TypeError):
            self.rectangle.width = 7.5

class TestRectangleHeightProperty(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_valid_height_setter(self):
        self.rectangle.height = 12
        self.assertEqual(self.rectangle.height, 12)

    def test_invalid_height_negative(self):
        with self.assertRaises(ValueError):
            self.rectangle.height = -8

    def test_invalid_height_type(self):
        with self.assertRaises(TypeError):
            self.rectangle.height = "invalid"

    def test_height_zero(self):
        with self.assertRaises(ValueError):
            self.rectangle.height = 0

    def test_height_float(self):
        with self.assertRaises(TypeError):
            self.rectangle.height = 7.5

class TestRectangleXProperty(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_valid_x_setter(self):
        self.rectangle.x = 4
        self.assertEqual(self.rectangle.x, 4)

    def test_invalid_x_negative(self):
        with self.assertRaises(ValueError):
            self.rectangle.x = -2

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            self.rectangle.x = "invalid"

    def test_x_zero(self):
        self.rectangle.x = 0
        self.assertEqual(self.rectangle.x, 0)

    def test_x_float(self):
        with self.assertRaises(TypeError):
            self.rectangle.x = 2.5

class TestRectangleYProperty(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_valid_y_setter(self):
        self.rectangle.y = 4
        self.assertEqual(self.rectangle.y, 4)

    def test_invalid_y_negative(self):
        with self.assertRaises(ValueError):
            self.rectangle.y = -2

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            self.rectangle.y = "invalid"

    def test_y_zero(self):
        self.rectangle.y = 0
        self.assertEqual(self.rectangle.y, 0)

    def test_y_float(self):
        with self.assertRaises(TypeError):
            self.rectangle.y = 2.5

class TestRectangleAreaMethod(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_valid_area(self):
        self.assertEqual(self.rectangle.area(), 50)

    def test_area_large_dimensions(self):
        large_rectangle = Rectangle(10**6, 10**6)
        self.assertEqual(large_rectangle.area(), 10**12)

class TestRectangleDisplayMethod(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(4, 3, 2, 1, 1)

    def test_display_offset(self):
        expected_output = "\n\n  ####\n  ####\n  ####\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.rectangle.y = 2
            self.rectangle.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_display_custom_symbol_not_supported(self):
        with self.assertRaises(TypeError):
            self.rectangle.display('#', '-')


class TestRectangleStrMethod(unittest.TestCase):
    def test_str_default(self):
        rectangle = Rectangle(5, 10, 2, 3, 1)
        self.assertEqual(str(rectangle), "[Rectangle] (1) 2/3 - 5/10")

    def test_str_custom_id(self):
        rectangle = Rectangle(3, 6, 1, 1, 42)
        self.assertEqual(str(rectangle), "[Rectangle] (42) 1/1 - 3/6")

    def test_str_large_dimensions(self):
        rectangle = Rectangle(1000, 500, 0, 0, 7)
        self.assertEqual(str(rectangle), "[Rectangle] (7) 0/0 - 1000/500")

    def test_str_no_id(self):
        rectangle = Rectangle(4, 8, 2, 2)
        self.assertEqual(str(rectangle), "[Rectangle] (2) 2/2 - 4/8")

class TestRectangleUpdateMethodArgs(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_update_all_args(self):
        self.rectangle.update(10, 8, 6, 4, 2)
        self.assertEqual(str(self.rectangle), "[Rectangle] (10) 4/2 - 8/6")

    def test_update_partial_args(self):
        self.rectangle.update(5, 7, 4)
        self.assertEqual(str(self.rectangle), "[Rectangle] (5) 2/3 - 7/4")

    def test_update_id_only(self):
        self.rectangle.update(20)
        self.assertEqual(str(self.rectangle), "[Rectangle] (20) 2/3 - 5/10")




class TestRectangleUpdateMethodKwargs(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(5, 10, 2, 3, 1)

    def test_update_all_kwargs(self):
        self.rectangle.update(id=10, width=8, height=6, x=4, y=2)
        self.assertEqual(str(self.rectangle), "[Rectangle] (10) 4/2 - 8/6")

    def test_update_partial_kwargs(self):
        self.rectangle.update(id=5, width=7, y=4)
        self.assertEqual(str(self.rectangle), "[Rectangle] (5) 2/4 - 7/10")

    def test_update_id_only(self):
        self.rectangle.update(id=20)
        self.assertEqual(str(self.rectangle), "[Rectangle] (20) 2/3 - 5/10")


if __name__ == '__main__':
    unittest.main()
