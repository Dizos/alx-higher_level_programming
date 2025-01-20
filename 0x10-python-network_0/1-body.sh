#!/bin/bash
# this Script shows the body of a 200 status code response
curl -s -w "%{http_code}" "$1" | grep -E '^200' -A 1 | tail -n 1
