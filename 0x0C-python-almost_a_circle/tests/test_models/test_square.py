#!/usr/bin/python3
"""
A unittest module for the square class
"""





import unittest
from unittest.mock import patch
from io import StringIO
from models.square import Square





class TestSquareInitialization(unittest.TestCase):
    def test_valid_initialization(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(square.size, 5)
        self.assertEqual(square.x, 2)
        self.assertEqual(square.y, 3)
        self.assertEqual(square.id, 1)

    def test_invalid_size_negative(self):
        with self.assertRaises(ValueError):
            Square(-5, 2, 3, 1)

    def test_invalid_x_negative(self):
        with self.assertRaises(ValueError):
            Square(5, -2, 3, 1)

    def test_invalid_y_negative(self):
        with self.assertRaises(ValueError):
            Square(5, 2, -3, 1)

    def test_invalid_id_negative(self):
        with self.assertRaises(ValueError):
            Square(5, 2, 3, -1)

    def test_invalid_size_type(self):
        with self.assertRaises(TypeError):
            Square("invalid", 2, 3, 1)

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            Square(5, "invalid", 3, 1)

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            Square(5, 2, "invalid", 1)

class TestSquareSizeProperty(unittest.TestCase):
    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_valid_size_setter(self):
        self.square.size = 8
        self.assertEqual(self.square.size, 8)

    def test_invalid_size_negative(self):
        with self.assertRaises(ValueError):
            self.square.size = -5

    def test_invalid_size_type(self):
        with self.assertRaises(TypeError):
            self.square.size = "invalid"

    def test_size_zero(self):
        with self.assertRaises(ValueError):
            self.square.size = 0

    def test_size_float(self):
        with self.assertRaises(TypeError):
            self.square.size = 7.5

class TestSquareXProperty(unittest.TestCase):
    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_valid_x_setter(self):
        self.square.x = 4
        self.assertEqual(self.square.x, 4)

    def test_invalid_x_negative(self):
        with self.assertRaises(ValueError):
            self.square.x = -2

    def test_invalid_x_type(self):
        with self.assertRaises(TypeError):
            self.square.x = "invalid"

    def test_x_zero(self):
        self.square.x = 0
        self.assertEqual(self.square.x, 0)

    def test_x_float(self):
        with self.assertRaises(TypeError):
            self.square.x = 2.5

class TestSquareYProperty(unittest.TestCase):
    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_valid_y_setter(self):
        self.square.y = 4
        self.assertEqual(self.square.y, 4)

    def test_invalid_y_negative(self):
        with self.assertRaises(ValueError):
            self.square.y = -2

    def test_invalid_y_type(self):
        with self.assertRaises(TypeError):
            self.square.y = "invalid"

    def test_y_zero(self):
        self.square.y = 0
        self.assertEqual(self.square.y, 0)

    def test_y_float(self):
        with self.assertRaises(TypeError):
            self.square.y = 2.5

class TestSquareAreaMethod(unittest.TestCase):
    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_valid_area(self):
        self.assertEqual(self.square.area(), 25)

class TestSquareDisplayMethod(unittest.TestCase):
    def setUp(self):
        self.square = Square(4, 2, 1, 1)

    def test_display_offset(self):
        expected_output = "\n\n  ####\n  ####\n  ####\n"
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            self.square.y = 2
            self.square.display()
        self.assertEqual(mock_stdout.getvalue(), expected_output)

class TestSquareStrMethod(unittest.TestCase):
    def test_str_default(self):
        square = Square(5, 2, 3, 1)
        self.assertEqual(str(square), "[Square] (1) 2/3 - 5")

    def test_str_custom_id(self):
        square = Square(3, 1, 1, 42)
        self.assertEqual(str(square), "[Square] (42) 1/1 - 3")

    def test_str_large_dimensions(self):
        square = Square(1000, 0, 0, 7)
        self.assertEqual(str(square), "[Square] (7) 0/0 - 1000")

    def test_str_no_id(self):
        square = Square(4, 2, 2)
        self.assertEqual(str(square), "[Square] (2) 2/2 - 4")

class TestSquareUpdateMethodArgs(unittest.TestCase):
    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_update_all_args(self):
        self.square.update(10, 8, 4, 2)
        self.assertEqual(str(self.square), "[Square] (10) 2/3 - 8")

    def test_update_partial_args(self):
        self.square.update(5, 7, 4)
        self.assertEqual(str(self.square), "[Square] (5) 2/3 - 7")

    def test_update_id_only(self):
        self.square.update(20)
        self.assertEqual(str(self.square), "[Square] (20) 2/3 - 5")

class TestSquareUpdateMethodKwargs(unittest.TestCase):
    def setUp(self):
        self.square = Square(5, 2, 3, 1)

    def test_update_all_kwargs(self):
        self.square.update(id=10, size=8, x=4, y=2)
        self.assertEqual(str(self.square), "[Square] (10) 4/2 - 8")

    def test_update_partial_kwargs(self):
        self.square.update(id=5, size=7, y=4)
        self.assertEqual(str(self.square), "[Square] (5) 2/4 - 7")

    def test_update_id_only(self):
        self.square.update(id=20)
        self.assertEqual(str(self.square), "[Square] (20) 2/3 - 5")

if __name__ == '__main__':
    unittest.main()
