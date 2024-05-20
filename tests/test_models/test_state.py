#!/usr/bin/python3
"""Test Module"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test cases for the State class."""

    def setUp(self):
        """Set up test environment"""
        self.state = State()

    def tearDown(self):
        """Tear down test environment"""
        del self.state

    def test_attributes(self):
        """Test if State has the correct attributes"""
        self.assertEqual(self.state.name, "")


if __name__ == "__main__":
    unittest.main()
