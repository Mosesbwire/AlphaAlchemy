#!/usr/bin/python3

"""
    Module: test_baseModel
    This module contains the unittests for the base model class
"""

from datetime import datetime, timedelta, timezone
from models.base_model import BaseModel
import unittest


class TestBaseModel(unittest.TestCase):
    """ Test the BaseModel class """

    def setUp(self):
        """ instantiates a baseModel instance to be used in the tests """
        self.base = BaseModel()

    def test_model_instantiation(self):
        """ test that object is correctly created """

        self.assertIs(type(self.base), BaseModel)

    def test_attribute_types(self):
        """ test that the object attributes are the correct types """
        attr_types = {
            "id": str,
            "created_at": datetime,
            "updated_at": datetime,
        }

        for attr, types in attr_types.items():
            with self.subTest(attr=attr, types=types):
                self.assertIn(attr, self.base.__dict__)
                self.assertIs(type(self.base.__dict__[attr]), types)
    
    def test_string_repr(self):
        """ test __str__ function """
        clsName = self.base.__class__.__name__
        id = self.base.id
        attr = str(self.base.__dict__)

        expected = f"[{clsName}] ({id}) {attr}"

        result = str(self.base)
        self.assertEqual(expected, result)

    def test_uuid(self):
        """ test uuid is unique for each object """
        baseInstance = BaseModel()
        expected = baseInstance.id
        result = self.base.id

        self.assertNotEqual(expected, result)

    def test_datetime_attributes(self):
        """ test datetime - created_at and updated_at should be in a given delta range"""
        created_at = self.base.created_at
        updated_at = self.base.updated_at
        time_now = datetime.now(timezone.utc)

        self.assertAlmostEqual(created_at, updated_at, delta=timedelta(minutes=2))
        self.assertAlmostEqual(created_at, time_now, delta=timedelta(minutes=2))
        self.assertAlmostEqual(updated_at, time_now, delta=timedelta(minutes=2))
    def test_to_dict(self):
        """ test conversion of object attributes to dictionary """
        instance_dict = self.base.to_dict()
        expected_attrs = ["id", "created_at", "updated_at"]
        date_format = "%Y-%m-%d %H:%M:%S.%f" 
        dict_created_at = instance_dict["created_at"]
        dict_updated_at = instance_dict["updated_at"]
       

        self.assertCountEqual(instance_dict.keys(), expected_attrs)
        self.assertEqual(instance_dict["id"], self.base.id)
        self.assertIsInstance(dict_created_at, str)
        self.assertIsInstance(dict_updated_at, str)
        self.assertIsInstance(instance_dict, dict)
       
        self.assertEqual(self.base.created_at, dict_created_at)
        self.assertEqual(self.base.updated_at, dict_updated_at)



         
