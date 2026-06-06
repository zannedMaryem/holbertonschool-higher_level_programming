#!/usr/bin/env python3
"""Basic serialization utilities."""

import json


def serialize_and_save_to_file(data, filename):
    """Serialize a Python dictionary to a JSON file.

    Args:
        data (dict): The data to serialize.
        filename (str): Path to the output JSON file.
    """
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """Load a JSON file and deserialize it to a Python dictionary.

    Args:
        filename (str): Path to the input JSON file.

    Returns:
        dict: The deserialized JSON data.
    """
    with open(filename, "r", encoding="utf-8") as file:
        return json.load(file)
