#!/bin/bash
# tis Script shows the allowed HTTP methods for a URL
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2-
