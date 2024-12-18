#!/bin/bash
flask db upgrade
exec gunicorn -b :5000 --access-logfile - --error-logfile - --timeout 600 main:app
