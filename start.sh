#!/bin/sh

python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py start_api_load
python3 manage.py runserver 0.0.0.0:8000