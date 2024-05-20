#!/usr/bin/python3
"""This module contains the Review class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review Class for review objects"""
    place_id = ""
    user_id = ""
    text = ""
