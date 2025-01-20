#!/bin/bash
# this script sends a GET request with X-School-User-Id header set to 98
curl -s -H "X-School-User-Id: 98" "$1"
