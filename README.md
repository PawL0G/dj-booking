First Launch:

1. Clone repo
2. Install env packages:
    - pip install django
    - pip install djangorestframework
3. Run following commands:
    - python manage.py migrate
    - python manage.py createsuperuser (create user for admin panel)
    - python manage.py runserver (launch server)

API was built with Django Rest Framework

1. Data based on ORM
2. Used Google Maps API as place determination by origin
3. Created two models with hotels and booking (as list)

Testing:

To test functionality goto 127.0.0.1/api/hotels

1. There is 4 methods GET/POST/PUT/DELETE
2. You can add your origin and hotel by desire (preferable to do it in django admin panel)
3. Check booking list go by  127.0.0.1/api/booking