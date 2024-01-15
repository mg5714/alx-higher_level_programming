#!/usr/bin/python3
"""Module for Base class"""
import json
import csv


class Base:
    """Represents the base class for all other classes in this project."""

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes new instance Base class.

        Args:
            id: The identifier for the instance. or None
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns JSON string representation oflist dictionaries"""
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Saves list of instances to json"""
        if list_objs is not None:
            list_objs = [obj.to_dictionary() for obj in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))

    @staticmethod
    def from_json_string(json_string):
        """Returns list of instances from JSON string representation"""
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Creates instance with all attributes already set"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = cls()

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Loads list of instances from JSON file"""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()
                list_dicts = cls.from_json_string(json_string)
                return [cls.create(**data) for data in list_dicts]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Saves list of instances to CSV file"""
        filename = f"{cls.__name__}.csv"
        try:
            data = [obj.to_csv_row() for obj in list_objs]
            with open(filename, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(["id", "width", "height", "x", "y"])
                writer.writerows(["id", "size", "x", "y"])
                writer.writerows(data)
        except FileNotFoundError:
            print(f"Error: Could not create file {filename}")

    @classmethod
    def load_from_file_csv(cls):
        """Loads a list of instances from a CSV file"""
        filename = f"{cls.__name__}.csv"
        instances = []
        try:
            with open(filename, "r") as file:
                reader = csv.reader(file)
                headers = next(reader)
                for row in reader:
                    instances.append(cls.from_csv_row(row))
        except FileNotFoundError:
            pass
        return instances
