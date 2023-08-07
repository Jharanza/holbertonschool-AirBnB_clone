#!/usr/bin/python3
import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest
import os


class TestFileStorage(unittest.TestCase):
    """file_path attribute test"""
    def test_file_path_is_none(self):
        file_path = FileStorage() #.__file_path
        self.assertIsNotNone(file_path, '__file_path is none')

    def test_file_path_attribute(self):
        file_storage = FileStorage()
        file_path = file_storage._FileStorage__file_path
        self.assertIsNotNone(file_path)

    def test_objects_attribute(self):
        file_storage = FileStorage()
        file_object = file_storage._FileStorage__objects
        text = "__file_object is not dictionary"
        self.assertIsInstance(file_object, dict, text)

    def test_all(self):
        file_storage = FileStorage()
        self.assertIsInstance(file_storage.all(), dict)

    def test_new(self):
        file_storage = FileStorage()
        base_model = BaseModel()
        key = "{}.{}".format(base_model.__class__.__name__, base_model.id)

        file_storage.new(base_model)
        self.assertIn(key, file_storage.all())

    def test_save(self):
        file_storage = FileStorage()

        file_storage.save()
        self.assertTrue(os.path.exists("file.json"))

    def test_reload(self):
        base_model = BaseModel()
        file_storage = FileStorage()
        file_storage.new(base_model)
        file_storage.reload()
        # self.assertEqual(len(file_storage.all()), 24)


if __name__ == '__main__':
    unittest.main()
