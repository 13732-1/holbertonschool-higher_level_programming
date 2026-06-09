#!/usr/bin/python3
"""
This module sends a POST request with an email parameter to a specified URL.

It parses parameters from sys arguments and displays the string response body.
"""
import sys
import urllib.parse
import urllib.request


def send_post_email():
    """
    Encodes the email parameter and executes a POST request to the target URL.
    
    Includes the mandatory firewall clearance header for secure transmission.
    """
    url = sys.argv[1]
    email_val = sys.argv[2]
    
    data = urllib.parse.urlencode({'email': email_val}).encode('ascii')
    headers = {
        'cfclearance': 'true'
    }
    
    req = urllib.request.Request(url, data=data, headers=headers)
    
    with urllib.request.urlopen(req) as response:
        html = response.read()
        print(html.decode('utf-8'))


if __name__ == "__main__":
    send_post_email()
