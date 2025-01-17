#!/usr/bin/python3
"""
Python script that takes in a URL and an email address,
sends a POST request to the passed URL with the email as a parameter,
and displays the body of the response.
"""
import sys
import urllib.request
import urllib.parse
import urllib.error


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    
    # Prepare the data for POST request
    data = urllib.parse.urlencode({'email': email}).encode('ascii')
    
    try:
        # Create the request and send it
        req = urllib.request.Request(url, data=data, method='POST')
        with urllib.request.urlopen(req) as response:
            # Read and decode the response body
            print(response.read().decode('utf-8'))
    except urllib.error.URLError as e:
        print(f"Error: {e.reason}")
