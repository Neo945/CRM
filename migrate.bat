pip install virtualenv
python -m venv venv

.\venv\Scripts\activate.bat

pip install -r requirements.txt

python manage.py makemigrations
python manage.py migrate

python manage.py collectstatic --noinput

python manage.py runserver