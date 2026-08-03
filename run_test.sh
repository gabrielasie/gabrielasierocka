#!/bin/bash
source "$(dirname "$0")/python3-virtualenv/bin/activate"
export TESTING=true
python3 -m unittest discover -v
