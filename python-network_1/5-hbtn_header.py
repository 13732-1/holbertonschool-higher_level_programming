#!/usr/bin/python3
"""
This module accepts a URL parameter, requests it, and prints a header.

It processes network operations via requests and extracts specific header meta.
"""
import sys
import requests


def get_header_id_requests():
    """
    Sends a GET request to a URL and displays the X-Request-Id header value.

    Uses the dictionary get method to safely query headers per requirements.
    """
    url = sys.argv[1]
    headers = {
        'cfclearance': 'true'
    }

    response = requests.get(url, headers=headers)
    print(response.headers.get('X-Request-Id'))


if __name__ == "__main__":
    get_header_id_requests()
