release: python manage.py makemigrations && python manage.py migrate

web: gunicorn src.family_star.wsgi
