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

Note: to test map API you need to switch page to admin https://django-app-booking.herokuapp.com/admin

1. Data based on ORM
2. Used Google Maps API as place determination by origin
3. Created two models with hotels and booking (as list)

Testing:

![plot](./api.png)

To test functionality goto https://django-app-booking.herokuapp.com/api/hotels

1. This endpoint using 4 methods GET/POST/PUT/DELETE
2. You can add your origin and hotel by desire (preferable to do it in django admin panel)
3. POST/PUT Method to add/update post id data

![plot](./api2.png)

To Check booking list go by  https://django-app-booking.herokuapp.com/api/booking

1. This endpoint using 1 method - GET
2. Extracting all bookings via GET method