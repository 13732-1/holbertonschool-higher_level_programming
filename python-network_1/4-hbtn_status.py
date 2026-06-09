#!/usr/bin/python3
"""
This module fetches status information from an intranet URL using requests.

It captures the response payload and logs details regarding its string data
type and underlying textual structure directly to standard output.
"""
import requests


def fetch_status_with_requests():
    """
    Queries the target endpoint via the third-party requests package.

    Includes the mandatory firewall clearance header for secure transmission.
    """
    url = "https://intranet.hbtn.io/status"
    headers = {
        'cfclearance': 'true'
    }

    response = requests.get(url, headers=headers)
    text_content = response.text

    print("Body response:")
    print("\t- type: {}".format(type(text_content)))
    print("\t- content: {}".format(text_content))


if __name__ == "__main__":
    fetch_status_with_requests()
