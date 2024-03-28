#!/bin/bash
# Send a request to 0.0.0.0:5000/catch_me with curl
curl -sL -X PUT -d "user_id=98" 0.0.0.0:5000/catch_me -H "Origin: You got me!"
