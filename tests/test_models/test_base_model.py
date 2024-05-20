#!/usr/bin/python3
"""Test module for BaseModel and FileStorage Classes"""
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestBaseModel(unittest.TestCase):
    """Unittests for testing the BaseModel class."""

    def setUp(self):
        """Set up test environment."""
        self.model = BaseModel()

    def test_instance_creation(self):
        """Test that a BaseModel instance is correctly created."""
        self.assertIsInstance(self.model, BaseModel)
        self.assertTrue(hasattr(self.model, "id"))
        self.assertTrue(hasattr(self.model, "created_at"))
        self.assertTrue(hasattr(self.model, "updated_at"))

    def test_save_method(self):
        """Test that save updates the updated_at attribute."""
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertNotEqual(old_updated_at, self.model.updated_at)

    def test_to_dict_method(self):
        """Test that to_dict returns the correct dictionary."""
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict["id"], self.model.id)
        self.assertEqual(model_dict["__class__"], "BaseModel")
        self.assertEqual(model_dict["created_at"],
                         self.model.created_at.isoformat())
        self.assertEqual(model_dict["updated_at"],
                         self.model.updated_at.isoformat())

    def test_recreate_from_dict(self):
        """Test that an instance can be recreated from a dictionary."""
        model_dict = self.model.to_dict()
        new_model = BaseModel(**model_dict)
        self.assertEqual(new_model.id, self.model.id)
        self.assertEqual(new_model.created_at, self.model.created_at)
        self.assertEqual(new_model.updated_at, self.model.updated_at)


if __name__ == "__main__":
    unittest.main()
