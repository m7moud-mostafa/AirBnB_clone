#!/usr/bin/python3
"""Test Module"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
    """Test cases for the Place class."""

    def setUp(self):
        """Set up test environment"""
        self.place = Place()

    def tearDown(self):
        """Tear down test environment"""
        del self.place

    def test_attributes(self):
        """Test if Place has the correct attributes"""
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.user_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])


if __name__ == "__main__":
    unittest.main()
