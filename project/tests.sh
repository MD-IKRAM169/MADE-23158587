#!/bin/bash
# ./project/ python tests.py
python -m unittest discover -s . -p '*_test.py'
chmod +x tests.sh
