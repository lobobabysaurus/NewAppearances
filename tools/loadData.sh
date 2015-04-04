#!/bin/sh
python3 ../manage.py loaddata home/homeData.yaml
python3 ../manage.py loaddata hours/hoursData.yaml
python3 ../manage.py loaddata products/productsData.yaml
python3 ../manage.py loaddata services/serviceData.yaml
