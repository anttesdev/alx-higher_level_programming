#!/usr/bin/python3
"""
Uniittest for base module
"""


import unittest
import os
import json
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestBaseInstantiation(unittest.TestCase):

    def test_base_instantiation(self):
        """Test Base class instantiation."""
        obj = Base()
        self.assertIsNotNone(obj.id)

    def test_base_instantiation_with_id(self):
        """Test Base class instantiation with a specified id."""
        obj = Base(id=10)
        self.assertEqual(obj.id, 10)

    def test_base_instantiation_multiple_objects(self):
        """Test multiple instances of Base with auto-incremented ids."""
        obj1 = Base()
        obj2 = Base()
        self.assertNotEqual(obj1.id, obj2.id)

    def test_base_instantiation_without_id(self):
        """Test Base instantiation without specifying an id."""
        obj = Base()
        self.assertIsNotNone(obj.id)

    def test_base_instantiation_default_id(self):
        """Test that the default id is auto-incremented."""
        obj1 = Base()
        obj2 = Base()
        self.assertEqual(obj1.id + 1, obj2.id)

    def test_base_instantiation_with_zero_id(self):
        """Test Base instantiation with id=0."""
        obj = Base(id=0)
        self.assertEqual(obj.id, 0)

    def test_base_instantiation_large_id(self):
        """Test Base instantiation with a large id."""
        obj = Base(id=1000000000)
        self.assertEqual(obj.id, 1000000000)

    def test_base_instantiation_with_boolean(self):
        """Test Base instantiation with a boolean id (should not raise an error)."""
        obj = Base(id=True)
        self.assertEqual(obj.id, True)

    def test_base_instantiation_with_dictionary(self):
        """Test Base instantiation with a dictionary id (should not raise an error)."""
        obj = Base(id={"key": "value"})
        self.assertEqual(obj.id, {"key": "value"})

    def test_base_instantiation_with_nan(self):
        """Test Base instantiation with NaN id (should not raise an error)."""
        import math
        obj = Base(id=math.nan)
        self.assertTrue(math.isnan(obj.id))

    def test_base_instantiation_with_tuple(self):
        """Test Base instantiation with a tuple id (should not raise an error)."""
        obj = Base(id=(1, 2, 3))
        self.assertEqual(obj.id, (1, 2, 3))

    def test_base_instantiation_with_list(self):
        """Test Base instantiation with a list id (should not raise an error)."""
        obj = Base(id=[1, 2, 3])
        self.assertEqual(obj.id, [1, 2, 3])

    def test_base_instantiation_with_complex_number(self):
        """Test Base instantiation with a complex number id (should not raise an error)."""
        obj = Base(id=1 + 2j)
        self.assertEqual(obj.id, 1 + 2j)

    def test_base_instantiation_with_float(self):
        """Test Base instantiation with a float id (should not raise an error)."""
        obj = Base(id=3.14)
        self.assertEqual(obj.id, 3.14)

    def test_base_instantiation_with_two_arguments(self):
        """Test Base instantiation with two arguments."""
        with self.assertRaises(TypeError):
            obj = Base(10, 20)
    
    def test_base_instantiation_with_infinity(self):
        """Test Base instantiation with infinity."""
        obj = Base(id=float('inf'))
        self.assertEqual(obj.id, float('inf'))

    def test_base_instantiation_with_string_id(self):
        """Test Base instantiation with a string id."""
        obj = Base(id="test_string")
        self.assertEqual(obj.id, "test_string")

class TestToJSONString(unittest.TestCase):
    def test_to_json_string_empty_list(self):
        result = Rectangle.to_json_string([])
        self.assertEqual(result, "[]")

    def test_to_json_string_single_rectangle(self):
        rectangle = Rectangle(2, 3, 1, 1, 99)
        result = Rectangle.to_json_string([rectangle.to_dictionary()])
        expected = '[{"x": 1, "y": 1, "id": 99, "height": 3, "width": 2}]'
        self.assertEqual(result, expected)

    def test_to_json_string_single_square(self):
        square = Square(2, 1, 1, 99)
        result = Square.to_json_string([square.to_dictionary()])
        expected = '[{"id": 99, "x": 1, "size": 2, "y": 1}]'
        self.assertEqual(result, expected)

    def test_to_json_string_multiple_shapes(self):
        rectangle = Rectangle(2, 3, 1, 1, 99)
        square = Square(2, 1, 1, 100)
        result = Rectangle.to_json_string([rectangle.to_dictionary(), square.to_dictionary()])
        expected = '[{"x": 1, "y": 1, "id": 99, "height": 3, "width": 2},' \
               '{"id": 100, "x": 1, "size": 2, "y": 1}]'


    def test_to_json_string_none_list(self):
        result = Rectangle.to_json_string(None)
        self.assertEqual(result, "[]")

    def test_to_json_string_default_values(self):
        rectangle = Rectangle(1, 1, 0, 0, 1)
        result = Rectangle.to_json_string([rectangle.to_dictionary()])
        expected = '[{"x": 0, "y": 0, "id": 1, "height": 1, "width": 1}]'
        self.assertEqual(result, expected)

    def test_to_json_string_min_valid_values(self):
        rectangle = Rectangle(1, 1, 0, 0, 1)
        result = Rectangle.to_json_string([rectangle.to_dictionary()])
        expected = '[{"x": 0, "y": 0, "id": 1, "height": 1, "width": 1}]'
        self.assertEqual(result, expected)

    def test_to_json_string_square_none_values(self):
        square = Square(1, 0, 0, 1)
        result = Square.to_json_string([square.to_dictionary()])
        expected = '[{"id": 1, "x": 0, "size": 1, "y": 0}]'

class TestBaseSaveToFile(unittest.TestCase):

    def test_save_to_file_rectangle(self):
        r1 = Rectangle(10, 8)
        r2 = Rectangle(2, 4)

        Rectangle.save_to_file([r1, r2])

        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", 'r') as file:
            content = file.read()
            loaded_data = Base.from_json_string(content)
            loaded_rectangles = [Rectangle.create(**d) for d in loaded_data]

        self.assertEqual(loaded_rectangles[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded_rectangles[1].to_dictionary(), r2.to_dictionary())

        os.remove("Rectangle.json")

    def test_save_to_file_square(self):
        s1 = Square(5)
        s2 = Square(3)

        Square.save_to_file([s1, s2])

        self.assertTrue(os.path.exists("Square.json"))

        with open("Square.json", 'r') as file:
            content = file.read()
            loaded_data = Base.from_json_string(content)
            loaded_squares = [Square.create(**d) for d in loaded_data]

        self.assertEqual(loaded_squares[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(loaded_squares[1].to_dictionary(), s2.to_dictionary())

        os.remove("Square.json")

    def test_save_to_file_empty_list(self):
        Rectangle.save_to_file([])
        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", 'r') as file:
            content = file.read()
            loaded_data = Base.from_json_string(content)

        self.assertEqual(loaded_data, [])

        os.remove("Rectangle.json")

    def test_save_to_file_no_list(self):
        Rectangle.save_to_file(None)
        self.assertTrue(os.path.exists("Rectangle.json"))

        with open("Rectangle.json", 'r') as file:
            content = file.read()
            loaded_data = Base.from_json_string(content)

        self.assertEqual(loaded_data, [])

        os.remove("Rectangle.json")

class TestBaseFromJsonString(unittest.TestCase):

    def test_from_json_string_rectangle(self):
        r1 = Rectangle(10, 8)
        r2 = Rectangle(2, 4)
        json_string = Rectangle.to_json_string([r1.to_dictionary(), r2.to_dictionary()])

        loaded_data = Rectangle.from_json_string(json_string)
        loaded_rectangles = [Rectangle.create(**d) for d in loaded_data]

        self.assertEqual(loaded_rectangles[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(loaded_rectangles[1].to_dictionary(), r2.to_dictionary())

    def test_from_json_string_square(self):
        s1 = Square(5)
        s2 = Square(3)
        json_string = Square.to_json_string([s1.to_dictionary(), s2.to_dictionary()])

        loaded_data = Square.from_json_string(json_string)
        loaded_squares = [Square.create(**d) for d in loaded_data]

        self.assertEqual(loaded_squares[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(loaded_squares[1].to_dictionary(), s2.to_dictionary())

    def test_from_json_string_empty_string(self):
        json_string = ""
        loaded_data = Base.from_json_string(json_string)
        self.assertEqual(loaded_data, [])

    def test_from_json_string_none(self):
        json_string = None
        loaded_data = Base.from_json_string(json_string)
        self.assertEqual(loaded_data, [])

    def test_from_json_string_empty_list(self):
        json_string = "[]"
        loaded_data = Base.from_json_string(json_string)
        self.assertEqual(loaded_data, [])

    def test_from_json_string_invalid_json(self):
        json_string = "invalid_json"
        with self.assertRaises(json.JSONDecodeError):
            loaded_data = Base.from_json_string(json_string)

    def test_from_json_string_invalid_json_dict(self):
        json_string = '{"key": "value", "key2": "value2"}'
        loaded_data = Base.from_json_string(json_string)
        self.assertEqual(loaded_data, {'key': 'value', 'key2': 'value2'})

    def test_from_json_string_invalid_json_list(self):
        json_string = '["invalid_json", "invalid_json"]'
        loaded_data = Base.from_json_string(json_string)
        self.assertEqual(loaded_data, ['invalid_json', 'invalid_json'])
class TestBaseCreate(unittest.TestCase):

    def test_create_rectangle(self):
        rectangle_dict = {'id': 1, 'width': 10, 'height': 5, 'x': 2, 'y': 3}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle_instance.id, rectangle_dict['id'])
        self.assertEqual(rectangle_instance.width, rectangle_dict['width'])
        self.assertEqual(rectangle_instance.height, rectangle_dict['height'])
        self.assertEqual(rectangle_instance.x, rectangle_dict['x'])
        self.assertEqual(rectangle_instance.y, rectangle_dict['y'])

    def test_create_square(self):
        square_dict = {'id': 2, 'size': 4, 'x': 1, 'y': 2}
        square_instance = Square.create(**square_dict)
        self.assertEqual(square_instance.id, square_dict['id'])
        self.assertEqual(square_instance.size, square_dict['size'])
        self.assertEqual(square_instance.x, square_dict['x'])
        self.assertEqual(square_instance.y, square_dict['y'])

    def test_create_missing_arguments(self):
        rectangle_dict = {'id': 3, 'width': 10, 'height': 5}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertEqual(rectangle_instance.x, 0)
        self.assertEqual(rectangle_instance.y, 0)

        square_dict = {'id': 4, 'size': 4}
        square_instance = Square.create(**square_dict)
        self.assertEqual(square_instance.x, 0)
        self.assertEqual(square_instance.y, 0)

    def test_create_extra_arguments(self):
        rectangle_dict = {'id': 5, 'width': 10, 'height': 5, 'x': 2, 'y': 3, 'extra': 'extra_value'}
        rectangle_instance = Rectangle.create(**rectangle_dict)
        self.assertTrue(hasattr(rectangle_instance, 'extra'))

        square_dict = {'id': 6, 'size': 4, 'x': 1, 'y': 2, 'extra': 'extra_value'}
        square_instance = Square.create(**square_dict)
        self.assertTrue(hasattr(square_instance, 'extra'))

class TestBaseLoadFromFile(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove("Rectangle.json")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.json")
        except FileNotFoundError:
            pass

    def test_load_from_file_with_different_parameters(self):
        r1 = Rectangle(3, 5, 1, 2, 101)
        r2 = Rectangle(6, 3, 2, 1, 202)
        Rectangle.save_to_file([r1, r2])
        lst = Rectangle.load_from_file()
        self.assertDictEqual(lst[0].to_dictionary(), r1.to_dictionary())
        self.assertEqual(type(lst[0]), Rectangle)
        self.assertDictEqual(lst[1].to_dictionary(), r2.to_dictionary())
        self.assertEqual(type(lst[1]), Rectangle)

        s1 = Square(4, 2, 101, 303)
        s2 = Square(7, 1, 202, 404)
        Square.save_to_file([s1, s2])
        lst = Square.load_from_file()
        self.assertDictEqual(lst[0].to_dictionary(), s1.to_dictionary())
        self.assertEqual(type(lst[0]), Square)
        self.assertDictEqual(lst[1].to_dictionary(), s2.to_dictionary())
        self.assertEqual(type(lst[1]), Square)

    def test_load_from_file_with_no_file(self):
        lst = Rectangle.load_from_file()
        self.assertEqual(lst, [])

    def test_load_from_file_with_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.load_from_file(42)

class TestBaseSaveToFileCSV(unittest.TestCase):

    def tearDown(self):
        try:
            os.remove("Rectangle.csv")
        except FileNotFoundError:
            pass
        try:
            os.remove("Square.csv")
        except FileNotFoundError:
            pass

    def test_save_to_file_csv_with_rectangles(self):
        r1 = Rectangle(3, 5, 1, 2, 101)
        r2 = Rectangle(6, 3, 2, 1, 202)
        Rectangle.save_to_file_csv([r1, r2])
        self.assertTrue(os.path.isfile("Rectangle.csv"))
        with open("Rectangle.csv", 'r') as file:
            content = file.read()
            self.assertIn("101,3,5,1,2", content)
            self.assertIn("202,6,3,2,1", content)

    def test_save_to_file_csv_with_squares(self):
        s1 = Square(4, 2, 101, 303)
        s2 = Square(7, 1, 202, 404)
        Square.save_to_file_csv([s1, s2])
        self.assertTrue(os.path.isfile("Square.csv"))
        with open("Square.csv", 'r') as file:
            content = file.read()
            self.assertIn("303,4,2,101", content)
            self.assertIn("404,7,1,202", content)

    def test_save_to_file_csv_with_too_many_args(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv([Rectangle(1, 2), Rectangle(3, 4)], 42)

    def test_save_to_file_csv_no_arguments(self):
        with self.assertRaises(TypeError):
            Rectangle.save_to_file_csv()


class TestBaseLoadFromFileCSV(unittest.TestCase):

    @classmethod
    def tearDownClass(cls):
        """Delete any created files."""
        try:
            os.remove("Rectangle.csv")
        except IOError:
            pass
        try:
            os.remove("Square.csv")
        except IOError:
            pass

    def test_load_from_file_csv_first_rect(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        rects_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect1), str(rects_output[0]))

    def test_load_from_file_csv_second_rect(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        rects_output = Rectangle.load_from_file_csv()
        self.assertEqual(str(rect2), str(rects_output[1]))

    def test_load_from_file_csv_rect_types(self):
        rect1 = Rectangle(10, 7, 2, 8, 1)
        rect2 = Rectangle(2, 4, 5, 6, 2)
        Rectangle.save_to_file_csv([rect1, rect2])
        output = Rectangle.load_from_file_csv()
        self.assertTrue(all(type(obj) == Rectangle for obj in output))

    def test_load_from_file_csv_first_square(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([square1, square2])
        squares_output = Square.load_from_file_csv()
        self.assertEqual(str(square1), str(squares_output[0]))

    def test_load_from_file_csv_second_square(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([square1, square2])
        squares_output = Square.load_from_file_csv()
        self.assertEqual(str(square2), str(squares_output[1]))

    def test_load_from_file_csv_square_types(self):
        square1 = Square(5, 1, 3, 3)
        square2 = Square(9, 5, 2, 3)
        Square.save_to_file_csv([square1, square2])
        output = Square.load_from_file_csv()
        self.assertTrue(all(type(obj) == Square for obj in output))


    def test_load_from_file_csv_more_than_one_arg(self):
        with self.assertRaises(TypeError):
            Base.load_from_file_csv([], 1)
    

if __name__ == '__main__':
    unittest.main()
