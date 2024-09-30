#! /bin/bash

# pip3 install flask_tutorial-1.0.0-py3-none-any.whl --target .
# pip3 install https://github.com/qiqilelebaobao/flask-hello.git --target .

cd hello
python3 -m venv .venv
. .venv/bin/activate
pip3 install -r requirements/requirements.txt
