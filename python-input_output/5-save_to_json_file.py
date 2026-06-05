#!/usr/bin/python3
"""This module is to write data into a file with JSON"""


import json


def save_to_json_file(my_obj, filename):
    """This function writes data o a file"""
    with open(filename, mode='w', encoding='utf-8') as file:
        json.dump(my_obj, file, indent=4, ensure_ascii=False)
