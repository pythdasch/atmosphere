#!/bin/bash
git pull origin master
source venv/bin/activate
./venv/bin/pip install -r requirements.txt
./manage.py collectstatic --noinput
./manage.py migrate
./manage.py compilemessages
