#!/bin/bash
# Send a request to 0.0.0.0:5000/catch_me with curl
curl -sX PUT 0.0.0.0:5000/catch_me -d "user_id=98" -L -H "Origin: You got me!"
