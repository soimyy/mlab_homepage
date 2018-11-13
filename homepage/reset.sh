#!/bin/bash
app=$1
cd $app
rm -fr migrations/*
cd ..
rm -fr db.sqlite3
python manage.py makemigrations $app
python manage.py migrate
python manage.py createsuperuser
