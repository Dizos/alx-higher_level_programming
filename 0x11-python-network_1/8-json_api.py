#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys


if __name__ == "__main__":
    # Set the letter parameter (q), default to empty string if no argument given
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    
    # URL for the POST request
    url = "http://0.0.0.0:5000/search_user"
    
    # Send POST request with the letter parameter
    response = requests.post(url, data={'q': q})
    
    try:
        # Try to parse the JSON response
        json_response = response.json()
        
        # Check if response is empty
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
            
    except ValueError:
        print("Not a valid JSON")
