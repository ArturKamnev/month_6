python manage.py makemigrations
python manage.py migrate
python manage.py collectstatic --noinput

exec gunicorn shop_api.wsgi:application --bind 0.0.0.0:8000
# python manage.py runserver 0.0.0.0:8000