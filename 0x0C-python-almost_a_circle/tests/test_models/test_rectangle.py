#!/usr/bin/python3
"""
This module contains unit tests for the Rectangle class.
"""
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Test cases for the Rectangle class."""

    def setUp(self):
        """Set up test cases."""
        self.rect1 = Rectangle(10, 2)
        self.rect2 = Rectangle(2, 10, 0, 0, 12)

    def test_initialization(self):
        """Test initialization of Rectangle instances."""
        self.assertEqual(self.rect1.width, 10)
        self.assertEqual(self.rect1.height, 2)
        self.assertEqual(self.rect2.id, 12)

    def test_area(self):
        """Test area calculation."""
        self.assertEqual(self.rect1.area(), 20)
        self.assertEqual(self.rect2.area(), 20)

    # Add more test methods here

if __name__ == "__main__":
    unittest.main()
