#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import os
import json

class TestFileStorage(unittest.TestCase):
    """Test cases for the FileStorage class."""

    def setUp(self):
        """Set up test environment"""
        self.storage = FileStorage()
        self.model = BaseModel()
        self.file_path = "file.json"

    def tearDown(self):
        """Tear down test environment"""
        del self.storage
        del self.model
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all(self):
        """Test if all method returns the correct dictionary"""
        self.storage.new(self.model)
        self.assertEqual(self.storage.all()["BaseModel." + self.model.id], self.model)

    def test_new(self):
        """Test if new method adds an object to __objects"""
        self.storage.new(self.model)
        self.assertIn("BaseModel." + self.model.id, self.storage.all())

    def test_save(self):
        """Test if save method serializes __objects to JSON file"""
        self.storage.new(self.model)
        self.storage.save()
        with open(self.file_path, "r") as file:
            data = json.load(file)
        self.assertIn("BaseModel." + self.model.id, data)

    def test_reload(self):
        """Test if reload method deserializes JSON file to __objects"""
        self.storage.new(self.model)
        self.storage.save()
        self.storage.reload()
        self.assertIn("BaseModel." + self.model.id, self.storage.all())

if __name__ == "__main__":
    unittest.main()
