#!/usr/bin/python3
"""Test for base_model class"""

from models.base_model import BaseModel
import unittest

my_model = BaseModel()


class TestBaseModel(unittest.TestCase):
    """test the base class"""
    def test_base_class(self):
        """testcase for the class"""
        self.assertEqual(type(my_model), BaseModel)


class TestSave(unittest.TestCase):
    """testing the save function"""
    def test_update(self):
        """test id the method updates the date"""
        my_model.name = "My First Model"
        my_model.my_number = 89
        first = my_model.updated_at
        my_model.save()
        second = my_model.updated_at
        self.assertFalse(first == second)


class TestDictToJson(unittest.TestCase):
    """test the converion of obj to dict"""
    def test_dict_to_json(self):
        """testcase to check dict making"""
        my_model_json = my_model.to_dict()
        print(my_model_json)
        print("JSON of my_model:")
        for key in my_model_json.keys():
            print("\t{}: ({}) - {}".format(
                key, type(my_model_json[key]), my_model_json[key]))
        self.assertTrue(my_model_json.__class__)


class TestInit(unittest.TestCase):
    """testing initialization"""
    def test__init__(self):
        """test init value"""
        pass

    def test__str__(self):
        """test if string gives correct output"""
        pass
