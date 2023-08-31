#!/usr/bin/python3

"""
    Module: convrsion
    Contains functions to convert currencies
"""
from decimal import Decimal

CENTS = 100

def to_cents(unit):
    """ converts currency to cents 
        
        Args:
            unit: amount to convert to cents
        Returns:
            int: number of cents
    """
    try:
        unit = float(unit)
    except ValueError:
        raise
    
    if unit < 0:
        msg = f"unit can not be a negative value: {unit}"
        raise ValueError(msg)

    return int(unit * CENTS)

def to_unit_currency(cents):
    """ converts cents to unit currency
        Args:
            cents: cents to be converted
        Returns:
            decimal: unit currency in decimal
    """
    try:
        cents = float(cents)
    except ValueError:
        raise

    if not cents.is_integer():
        msg = f"cents must be an integer: {cents}"

        raise ValueError(msg)
    if cents < 0:
        msg = f"cents can not be a negative value: {cents}"
        raise ValueError(msg)

    cents = int(cents)

    decimal = Decimal(cents)

    return round(decimal/ CENTS, 2)

