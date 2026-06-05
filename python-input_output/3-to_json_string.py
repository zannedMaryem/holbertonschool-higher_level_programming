#!/usr/bin/python3
"""This module is to serialize an object"""

import json


def to_json_string(my_obj):
    """This function serializes an object to a text"""
    return json.dumps(my_obj)
