#!/usr/bin/python3
"""
This module sends a search parameter to an API endpoint using requests.

It handles empty arguments by defaulting the query variable, parses the response
as JSON payload data safely, and reports structured information or error tokens.
"""
import sys
import requests


def search_user_api():
    """
    Sends a POST request to a search API with a character parameter.
    
    Safe lookup is performed using the required dictionary get approach.
    """
    url = "http://0.0.0.0:5000/search_user"
    
    if len(sys.argv) > 1:
        q_val = sys.argv[1]
    else:
        q_val = ""

    payload = {'q': q_val}
    headers = {
        'cfclearance': 'true'
    }

    try:
        response = requests.post(url, data=payload, headers=headers)
        json_data = response.json()
        
        if not json_data:
            print("No result")
        else:
            user_id = json_data.get('id')
            user_name = json_data.get('name')
            print("[{}] {}".format(user_id, user_name))
            
    except ValueError:
        print("Not a valid JSON")


if __name__ == "__main__":
    search_user_api()
