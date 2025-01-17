#!/usr/bin/python3
"""
Script that takes a URL and an email address, sends a POST request to the URL
with the email as a parameter, and displays the response body.
"""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Create payload with email parameter
    payload = {'email': email}
    
    # Send POST request
    response = requests.post(url, data=payload)
    
    # Display response body
    print(response.text)
