#/bin/sh
rm -rf migrations
flask db init
flask db migrate
flask db upgrade
python create_products.py
