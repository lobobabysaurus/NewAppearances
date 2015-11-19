#!/usr/bin/env bash
cd ..
git pull origin master
node_modules/.bin/gulp build-both
sudo service apache2 stop
sudo rm -r /var/www/html/newapp2/*
sudo cp -r ./* /var/www/html/newapp2/
sudo cp ./../prod_settings.py /var/www/html/newapp2/NewAppearances/settings.py
sudo python3 /var/www/html/newapp2/manage.py collectstatic
sudo service apache2 start
sudo service apache2 reload
