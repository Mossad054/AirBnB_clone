#!/usr/bin/python3
import unittest
from models import city

""""
a test module to check  City class
"""


class Test_city(unittest.TestCase):
    """
    testing city class.
    """

    def setUp(self):
        """
        a setup method to create city object to be tested
        
        """

        self.city_obj = city.City()

    def tearDown(self):
        """
         teardown method that deletes the city object
        
        """
        del self.city_obj

    def test_instantiation(self):
        """
        test that the City object is instantiated correctly
        """
        self.assertIsInstance(self.city_obj, city.City)
        self.assertTrue(hasattr(self.city_obj, 'id'))
        self.assertTrue(hasattr(self.city_obj, 'created_at'))
        self.assertTrue(hasattr(self.city_obj, 'updated_at'))
        self.assertTrue(hasattr(self.city_obj, 'name'))

    def str_rep(self):
        """
        tests the __str__ method
        """
        str_rep = str(self.city_obj)
        self.assertIn('id', str_rep)
        self.assertIn(self.city_obj, str_rep)
        self.assertIn('created_at', str_rep)
        self.assertIn('updated_at', str_rep)
        self.assertIn('name', str_rep)

    def to_dict(self):
        """tests the to_dict method"""
        obj_dict = self.city_obj.to_dict()
        self.assertIsInstance(obj_dict, dict)
        self.assertIn('id', obj_dict)
        self.assertIn('name', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)


if '__name__' == '__main__':
    unittest.main()
