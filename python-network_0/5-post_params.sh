#!/bin/bash
# Sends a POST request to a URL with specific variables and displays the body.
curl -s -d "email=test@gmail.com" --data-urlencode "subject=I will always be here for PLD" "$1"
