#!/bin/bash

cd /home/lev/Netology/stocks_products
git pull origin main
source ../net_env/bin/activate
pip install -r requirements.txt
python3 manage.py migrate
deactivate
sudo systemctl restart gunicorn
