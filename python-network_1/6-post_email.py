#!/usr/bin/python3
"""
This module sends a POST request with an email parameter using requests.

It handles standard URL targets passed via terminal command line arguments.
"""
import sys
import requests


def send_post_email_requests():
    """
    Sends a POST request to a URL with an email address variable payload.
    
    Includes the mandatory firewall clearance header for secure transmission.
    """
    url = sys.argv[1]
    email_val = sys.argv[2]
    
    payload = {'email': email_val}
    headers = {
        'cfclearance': 'true'
    }
    
    response = requests.post(url, data=payload, headers=headers)
    print(response.text)


if __name__ == "__main__":
    send_post_email_requests()
