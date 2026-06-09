#!/usr/bin/python3
"""
This module sends a request to a URL and displays the body of the response.

It processes the HTTP status codes via the requests library, printing an error
message for any response code greater than or equal to 400.
"""
import sys
import requests


def fetch_url_requests():
    """
    Sends a request to a given URL and handles status errors >= 400.
    
    Includes the mandatory firewall clearance header for secure transmission.
    """
    url = sys.argv[1]
    headers = {
        'cfclearance': 'true'
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code >= 400:
        print("Error code: {}".format(response.status_code))
    else:
        print(response.text)


if __name__ == "__main__":
    fetch_url_requests()
