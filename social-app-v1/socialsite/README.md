**_Technologies_**

    - Python
    - Django

**_Installed Libraries_**

    - pip install django-braces
    - pip install django_bootstrap4
    - pip install django-humanize
    - pip install misaka 
        - possible error: Microsoft Visual C++ 14.0 is required in local
        - solution: https://www.scivision.dev/python-windows-visual-c-14-required/

**_Setup Instructions_**

    - python manage.py migrate
    - python manage.py makemigrations blog
    - python manage.py migrate
    - python manage.py createsuperuser
    - python manage.py runserver