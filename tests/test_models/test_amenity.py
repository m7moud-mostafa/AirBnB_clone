#!/usr/bin/python3
"""Test Module"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Test cases for the Amenity class."""

    def setUp(self):
        """Set up test environment"""
        self.amenity = Amenity()

    def tearDown(self):
        """Tear down test environment"""
        del self.amenity

    def test_attributes(self):
        """Test if Amenity has the correct attributes"""
        self.assertEqual(self.amenity.name, "")


if __name__ == "__main__":
    unittest.main()
