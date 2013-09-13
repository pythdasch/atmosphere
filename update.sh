#!/bin/bash
git pull origin master
source venv/bin/activate
pip install -r requirements.txt
./manage.py collectstatic --noinput
./manage.py migrate
./manage.py compilemessages
./manage.py sync_translation_fields
