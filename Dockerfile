FROM python:3
WORKDIR /usr/src/app
ADD requirements.txt /usr/src/app
pip install -r requirements.txt
ADD . /usr/src/app
