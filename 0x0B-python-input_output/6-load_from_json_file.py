#!/usr/bin/python3
"""define function"""


import json


def load_from_json_file(filename):
    """creates an Object from a “JSON file”"""
    with open(filename, 'r') as file:
        json_data = file.read()
        return json.loads(json_data)
