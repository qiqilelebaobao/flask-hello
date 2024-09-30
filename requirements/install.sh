#! /bin/bash

python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements.txt
pip3 install flask_tutorial-1.0.0-py3-none-any.whl --target .