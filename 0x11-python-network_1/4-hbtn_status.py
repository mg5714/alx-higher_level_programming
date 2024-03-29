#!/usr/bin/python3
""" script that fetches https://alx-intranet.hbtn.io/status"""
import requests

if __name__ == "__main__":
    url = 'https://alx-intranet.hbtn.io/status'
    response = requests.get(url)
    data = response.json()

    print("Body response:")
    print("\t- type:", type(data))
    print("\t- content:", data)
