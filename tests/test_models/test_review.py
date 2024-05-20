#!/usr/bin/python3
"""Test Module"""
import unittest
from models.review import Review


class TestReview(unittest.TestCase):
    """Test cases for the Review class."""

    def setUp(self):
        """Set up test environment"""
        self.review = Review()

    def tearDown(self):
        """Tear down test environment"""
        del self.review

    def test_attributes(self):
        """Test if Review has the correct attributes"""
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")


if __name__ == "__main__":
    unittest.main()
