realtime
========

Realtime waterlevel data

# Installation

Clone the repository with git and change to this folder

cd /opt;git clone https://github.com/VincentHussey/dev-realtime.git;cd /opt/dev-realtime

Create a virtual environment called env

virtualenv env

Activate it

source env/bin/activate

Install requirements

pip install -r requirements.txt

This project uses django.contrib.gis and so requires postgis, gdal, proj and geos to be installed.

Create a database.  A script has been prepared for this, it should be run as postgres. You will be prompted to create a user, twice for a password and then for a database name.  The script doesn't check if the user exists (not a problem), or if the database exists (generates lots of errors).

su postgres

utils/create_database.sh


