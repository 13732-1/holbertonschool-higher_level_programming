#!/usr/bin/python3
"""
This module sends a request to a URL and displays the body of the response.

It catches and handles urllib.error.HTTPError exceptions gracefully to print
the corresponding HTTP status code back to the standard output structure.
"""
import sys
import urllib.error
import urllib.request


def fetch_url_safely():
    """
    Requests the target URL and handles standard HTTP errors seamlessly.

    Includes the mandatory firewall clearance header for secure transmission.
    """
    url = sys.argv[1]
    headers = {
        'cfclearance': 'true'
    }

    req = urllib.request.Request(url, headers=headers)

    try:
        with urllib.request.urlopen(req) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except urllib.error.HTTPError as error:
        print("Error code: {}".format(error.code))


if __name__ == "__main__":
    fetch_url_safely()
