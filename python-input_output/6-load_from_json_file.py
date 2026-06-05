#!/usr/bin/python3
"""This module creates object from JSON file"""


import json


def load_from_json_file(filename):
    """This function creates an object from json file"""
    with open(filename, encoding='utf-8') as file:
        return json.load(file)
