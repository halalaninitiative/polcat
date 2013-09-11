polcat
======

The Politician Catalog

Installation
------------

1. Create PostgreSQL user and database and change settings.py accordingly.
2. `$ sudo apt-get install virtualenvwrapper`
3. `$ sudo apt-get install python-dev libpq-dev #for psycopg2`
4. `$ mkvirtualenv polcat`
5. `$ pip install -r requirements.txt`
6. `$ python manage.py syncdb`
7. `$ python manage.py migrate`

To Run
------

1. `$ workon polcat`
2. `$ pip install -r requirements.txt`
3. `$ python manage.py syncdb`
4. `$ python manage.py migrate`
5. `$ python manage.py runserver`
6. Access localhost:8000 using any browser.
