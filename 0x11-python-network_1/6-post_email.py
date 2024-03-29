#!/usr/bin/python3
"""POST request to a given URL with a given email
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    data = {"email": sys.argv[2]}

    res = requests.post(url, data=data)
    print(res.text)
