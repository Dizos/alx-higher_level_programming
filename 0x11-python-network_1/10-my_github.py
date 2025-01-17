#!/usr/bin/python3
"""
Script that takes GitHub credentials (username and personal access token)
and uses the GitHub API to display user id.
"""
import requests
import sys


if __name__ == "__main__":
    # Get username and token from command line arguments
    username = sys.argv[1]
    token = sys.argv[2]
    
    # GitHub API URL
    url = "https://api.github.com/user"
    
    # Send GET request with Basic Authentication
    response = requests.get(url, auth=(username, token))
    
    # Print the id from JSON response, None if not found
    print(response.json().get('id'))
