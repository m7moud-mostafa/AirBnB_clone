#!/usr/bin/python3
"""Test Module"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """Test cases for the User class."""

    def setUp(self):
        """Set up test environment"""
        self.user = User()

    def tearDown(self):
        """Tear down test environment"""
        del self.user

    def test_attributes(self):
        """Test if User has the correct attributes"""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")


if __name__ == "__main__":
    unittest.main()
