#!/usr/bin/python3
"""
This module uses the GitHub API to display the user id of a given account.

It authenticates using HTTP Basic Authentication via requests and parses the
resulting JSON object to securely extract the identity attribute.
"""
import sys
import requests


def display_github_id():
    """
    Sends a GET request to the GitHub API using Basic Authentication credentials.
    
    Safe lookup is performed using the required dictionary get approach.
    """
    username = sys.argv[1]
    token = sys.argv[2]
    
    url = "https://api.github.com/user"
    headers = {
        'cfclearance': 'true'
    }
    
    response = requests.get(url, auth=(username, token), headers=headers)
    user_data = response.json()
    
    print(user_data.get('id'))


if __name__ == "__main__":
    display_github_id()
