#!/bin/bash
# Script that sends a JSON POST request with contents from a file
curl -s -H "Content-Type: application/json" -X POST -d @"$2" "$1"
