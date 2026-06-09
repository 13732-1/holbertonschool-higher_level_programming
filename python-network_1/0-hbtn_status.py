#!/usr/bin/python3
"""
This module fetches status information from a specific intranet URL.

It utilizes the urllib package to safely query the endpoint and prints
well-formatted details about the response payload type and contents.
"""
import urllib.request


def fetch_status():
    """
    Fetches the status page and displays the breakdown of the response body.

    Includes the mandatory firewall clearance header for secure transmission.
    """
    url = "https://intranet.hbtn.io/status"
    headers = {
        'cfclearance': 'true'
    }

    req = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(req) as response:
        html = response.read()
        print("Body response:")
        print("\t- type: {}".format(type(html)))
        print("\t- content: {}".format(html))
        print("\t- utf8 content: {}".format(html.decode('utf-8')))


if __name__ == "__main__":
    fetch_status()
