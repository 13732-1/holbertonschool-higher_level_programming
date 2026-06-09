#!/usr/bin/python3
"""
This module takes a URL argument, requests it, and extracts a header value.

It targets the 'X-Request-Id' key from the network response header dictionary.
"""
import sys
import urllib.request


def get_header_id():
    """
    Sends a request to the given URL and prints the X-Request-Id header.

    Safe lookup is performed using the required dictionary get approach.
    """
    url = sys.argv[1]
    headers = {
        'cfclearance': 'true'
    }

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        info = response.info()
        print(info.get('X-Request-Id'))


if __name__ == "__main__":
    get_header_id()
