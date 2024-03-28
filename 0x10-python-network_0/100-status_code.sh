#!/bin/bash
# Sends a request to a URL and displays only the status code of the response

# Send the request and save the response headers to a temporary file
curl -s -o response_headers.txt -w "%{http_code}" "$1" > /dev/null
