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

This project uses django.contrib.gis and so requires gdal, proj and geos to be installed.
