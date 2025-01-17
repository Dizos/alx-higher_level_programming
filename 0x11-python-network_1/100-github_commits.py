#!/usr/bin/python3
"""
Script that lists 10 most recent commits of a GitHub repository
by a specific user using the GitHub API.
"""
import requests
import sys


if __name__ == "__main__":
    # Get repository and owner names from command line arguments
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]
    
    # GitHub API URL for commits
    url = f"https://api.github.com/repos/{owner_name}/{repo_name}/commits"
    
    # Send GET request with parameters to limit to 10 commits
    response = requests.get(url, params={'per_page': 10})
    
    # Print commits in required format
    for commit in response.json():
        sha = commit.get('sha')
        author_name = commit.get('commit').get('author').get('name')
        print(f"{sha}: {author_name}")
