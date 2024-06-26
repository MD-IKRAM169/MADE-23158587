#!/bin/bash
# ./project/ python tests.py
python -m unittest discover -s . -p '*_tests.py'
chmod +x tests.sh
./tests.sh
