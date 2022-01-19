import os

os.system('gunicorn -w 4 --bind 0.0.0.0:8000 wsgi:app --timeout 180')
