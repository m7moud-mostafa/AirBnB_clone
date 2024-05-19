#!/usr/bin/python3
"""This module contains the User Class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for user object"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
