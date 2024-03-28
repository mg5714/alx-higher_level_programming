#!/bin/bash
# Send a request to 0.0.0.0:5000/catch_me with curl
curl -o /dev/null -sw "You got me!" 0.0.0.0:5000/catch_me
