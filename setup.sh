#!/bin/bash

sudo ln ./app/http_ping.py /usr/local/bin/http_ping
sudo chmod +x /usr/local/bin/http_ping
pip install -r requirements.txt