Command to install things:
conda install django
conda install postgresql
conda install -c conda-forge django-environ
conda install psycopg2
conda install Pillow
<!-- conda install -c conda-forge opencv --> Fail, can't find .xml file for the model.
pip install opencv-python

Command to start:
python manage.py migrate
python manage.py collectstatic
python manage.py runserver
