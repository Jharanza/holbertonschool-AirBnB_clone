#!/usr/bin/python3
"""Unittests for BaseModel"""

import unittest
from models.base_model import BaseModel
import datetime

class TestBaseModel(unittest.TestCase):
    """Unittests for BaseModel"""
    def test_instantiate(self):
        """Pass instantiate"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        """Pass public id string format"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        """Pass created at datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        """Pass updated at datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_uid(self):
        """UID created at each instantiation"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_str(self):
        """___str__ method is string"""
        base1 = BaseModel()
        self.assertEqual(type(str(base1)), str)

    def test_save(self):
        """save method"""
        base1 = BaseModel()
        update = base1.updated_at
        base1.save()
        self.assertNotEqual(update, base1.updated_at)

    def test_to_dict(self):
        """Pass to_dict method"""
        base1 = BaseModel()
        self.assertTrue(dict, type(base1.to_dict))


if __name__ == "__main__":
    unittest.main()
