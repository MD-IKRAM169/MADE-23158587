#!/bin/bash
python -m unittest discover -s . -p 'tests.py'
chmod +x tests.sh
        ./tests.sh
