#!/bin/bash
# This Script displays the size of the responses from the body of a URL in bytes
curl -s "$1" | wc -c
