#!/usr/bin/python3
"""Test module for BaseModel and FileStorage Classes"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """Unittests for testing the FileStorage class."""

    def setUp(self):
        """Set up test environment."""
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = "test_file.json"
        self.storage._FileStorage__objects = {}

    def tearDown(self):
        """Remove test file."""
        if os.path.exists("test_file.json"):
            os.remove("test_file.json")

    def test_all_method(self):
        """Test that all returns the correct dictionary."""
        self.assertEqual(self.storage.all(), {})

    def test_new_method(self):
        """Test that new correctly adds an object."""
        model = BaseModel()
        self.storage.new(model)
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, self.storage.all())
        self.assertEqual(self.storage.all()[key], model)

    def test_save_method(self):
        """Test that save correctly serializes objects to JSON file."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        with open("test_file.json", "r") as f:
            content = json.load(f)
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, content)
        self.assertEqual(content[key]["id"], model.id)
        self.assertEqual(content[key]["__class__"], "BaseModel")

    def test_reload_method(self):
        """Test that reload correctly deserializes objects from JSON file."""
        model = BaseModel()
        self.storage.new(model)
        self.storage.save()
        self.storage._FileStorage__objects = {}
        self.storage.reload()
        key = f"{model.__class__.__name__}.{model.id}"
        self.assertIn(key, self.storage.all())
        reloaded_model = self.storage.all()[key]
        self.assertEqual(reloaded_model.id, model.id)
        self.assertEqual(reloaded_model.created_at, model.created_at)
        self.assertEqual(reloaded_model.updated_at, model.updated_at)


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
