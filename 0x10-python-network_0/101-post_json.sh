#!/bin/bash
# Send JSON POST request and display the response body
curl -sX POST "$1" -H "Content-Type: application/json" -d @"$2"
