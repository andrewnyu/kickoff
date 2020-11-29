#!/bin/sh
source venv/bin/activate
flask db upgrade
python init_db.py
exec gunicorn -b:5000 --access-logfile - --error-logfile - kickoff:app