#!/usr/bin/python3
"""Test Module"""
import unittest
from models.city import City


class TestCity(unittest.TestCase):
    """Test cases for the City class."""

    def setUp(self):
        """Set up test environment"""
        self.city = City()

    def tearDown(self):
        """Tear down test environment"""
        del self.city

    def test_attributes(self):
        """Test if City has the correct attributes"""
        self.assertEqual(self.city.state_id, "")
        self.assertEqual(self.city.name, "")


if __name__ == "__main__":
    unittest.main()
