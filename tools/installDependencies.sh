#!/usr/bin/env bash

sudo apt-get install python3-pip python-dev libmysqlclient-dev libjpeg-dev python-epydoc  python3-docutils \
                     npm mysql-server mysql-workbench git openjdk-7-jre
sudo pip3 install -r requirements.txt
sudo npm install -g http-server yuidocjs
