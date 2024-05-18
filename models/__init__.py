#!/usr/bin/python3
"""Initialization file for the models Package"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
