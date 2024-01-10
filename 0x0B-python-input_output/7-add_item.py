#!/usr/bin/python3
"""define script"""

import sys
import json


from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

arguments = sys.argv[1:]

existing_items = load_from_json_file("add_item.json")
all_items = list(set(existing_items + arguments))
save_to_json_file(all_items, "add_item.json")
print("Arguments saved to add_item.json")
