import json
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import unittest


class TestFileStorage(unittest.TestCases):

    def test_file_path_is_none(self):
        file_path = fileStorage.__file_path
        self.assertIsNotNone(file_path, '__file_path is none')
