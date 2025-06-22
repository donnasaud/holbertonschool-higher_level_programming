#!/usr/bin/python3
"""
This module provides a function that converts
a JSON string to a Python data structure.
"""

import json


def from_json_string(my_str):
    """Returns a Python object from a JSON string"""
    return json.loads(my_str)
