#/bin/sh
rm -rf migrations
flask db init
lask db migrate
flask db upgrade
python create_products.py
