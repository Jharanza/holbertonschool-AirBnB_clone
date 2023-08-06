#!/usr/bin/python3
"""The init file for the models dir"""
from models.engine.file_storage import FileStorage

storage = FileStorage()

storage.reload()
