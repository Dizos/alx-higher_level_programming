#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL and displays the body
of the response. If the HTTP status code is >= 400, it prints the error code.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    
    # Send GET request to the URL
    response = requests.get(url)
    
    # Check if status code is >= 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
