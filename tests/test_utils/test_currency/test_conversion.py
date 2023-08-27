#!/usr/bin/python3

"""
    Module: test_conversion
    Contains test for the conversion module
"""
from decimal import Decimal
import unittest
from utils.currency.conversion import to_cents, to_unit_currency


class TestConversion(unittest.TestCase):
    """ Contains unittest for the currency conversion module """
    
    def setUp(self):
        """ set up common values """
        self.cents = 100

    def test_to_cents_returns_integer(self):
        """ test return value is integer """
        actual = to_cents(45.06)

        self.assertIsInstance(actual, int)

    def test_to_cents(self):
        """ test that a unit currency is converted to cents """
    
        units = [100, 56.05, 0.98, 0.05, 100.52, "0.56", "500.36", 1]
        
        for unit in units:
            with self.subTest(unit = unit):
                expected = int(float(unit) * self.cents)
                actual = to_cents(unit)
                self.assertEqual(actual, expected)

    def test_to_cents_raise_value_error(self):
        """ test ValueError exception is raised if value is not numeric """

        units = ["str", " ",-0.56, -100, "-23", "-5.50"]

        for unit in units:
            with self.subTest(unit = unit):
                self.assertRaises(ValueError, to_cents, unit)


    def test_to_unit_currency_retuns_decimal(self):
        """ test return value is a decimal """
        actual = to_unit_currency("4506")

        self.assertIsInstance(actual, Decimal)

    def test_to_unit_currency(self):
        """ test that cents are converted back to unit currency value """

        cents = [1000, 50, "50", 0, "106", 98, 50036, "10", 1 ]

        expected = [10.00, 0.50, 0.50, 0.00, 1.06, 0.98, 500.36, 0.10, 0.01]

        for idx, unit in enumerate(cents):
            with self.subTest(unit = unit):
                actual = to_unit_currency(unit)
                self.assertEqual(float(actual), expected[idx])

    def test_to_unit_currency_raise_value_error(self):
        """ test ValueError is raised if argument is not int """

        invalid_cents = [" ", "3.14", 45550.06, -2300, "-10000", "cents", 500.36]

        for cents in invalid_cents:
            with self.subTest(cents = cents):
                self.assertRaises(ValueError, to_unit_currency, cents)
