#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for the max_integer function."""

    def test_ordered_list(self):
        """Test an ordered list of integers."""
        ordered = [1, 2, 3, 4]
        self.assertEqual(max_integer(ordered), 4)

    def test_unordered_list(self):
        """Test an unordered list of integers."""
        unordered = [1, 3, 4, 2]
        self.assertEqual(max_integer(unordered), 4)

    def test_empty_list(self):
        """Test an empty list."""
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_single_element_list(self):
        """Test a list with a single element."""
        single_element = [5]
        self.assertEqual(max_integer(single_element), 5)

    def test_float_numbers(self):
        """Test a list with float numbers."""
        floats = [1.53, 6.33, -9.123, 15.2, 6.0]
        self.assertEqual(max_integer(floats), 15.2)

    def test_int_and_float(self):
        """Test a list with both integers and floats."""
        int_float = [1.53, 15.5, -9, 15, 6]
        self.assertEqual(max_integer(int_float), 15.5)

    def test_string(self):
        """Test a string."""
        string = "Hello"
        self.assertEqual(max_integer(string), 'o')

    def test_list_of_strings(self):
        """Test a list of strings."""
        strings = ["Hello", "World"]
        self.assertEqual(max_integer(strings), "World")

    def test_empty_string(self):
        """Test an empty string."""
        self.assertEqual(max_integer(""), None)

    def test_max_at_beginning(self):
        """Test a list with max value at the beginning."""
        max_at_beginning = [4, 3, 2, 1]
        self.assertEqual(max_integer(max_at_beginning), 4)

    def test_max_at_middle(self):
        """Test a list with max value in the middle."""
        max_at_middle = [1, 3, 4, 2]
        self.assertEqual(max_integer(max_at_middle), 4)

    def test_negative_numbers(self):
        """Test a list of negative numbers."""
        negative = [-1, -2, -3, -4]
        self.assertEqual(max_integer(negative), -1)

    def test_large_list(self):
        """Test a large list."""
        large = list(range(1000000))
        large.append(1000001)
        self.assertEqual(max_integer(large), 1000001)

    def test_list_of_one_negative(self):
        """Test a list with a single negative number."""
        one_negative = [-5]
        self.assertEqual(max_integer(one_negative), -5)

    def test_non_list_argument(self):
        """Test handling of a non-list argument."""
        with self.assertRaises(TypeError):
            max_integer(None)


if __name__ == '__main__':
    unittest.main()
