#!/usr/bin/python3
"""
this Python script takes in a URL, sends a request and displays
the value of the X-Request-Id variable found in the header.
"""
import sys
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    with urllib.request.urlopen(url) as response:
        print(response.headers.get('X-Request-Id'))
