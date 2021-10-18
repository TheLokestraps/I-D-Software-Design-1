#!/bin/sh
sudo apt install python3-pip
pip install Django==2.2.3
django-admin startproject Premiun
python3 Premiun/manage.py migrate