#!/usr/bin/python3
"""User script"""

from models.base_model import BaseModel


class User(BaseModel):
    """ define airbnb users """
    email = ''
    password = ''
    first_name = ''
    last_name = ''
