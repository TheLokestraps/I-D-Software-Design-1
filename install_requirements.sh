#!/bin/sh
sudo apt install python3-pip
pip install Django==2.2.3
pip install django-allauth
pip install django-mptt
django-admin startproject Premiun
python3 Premiun/manage.py migrate
