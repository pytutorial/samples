How to create this blank project :

I.Run command:
  1. django-admin startproject mysite
  2. cd mysite
  3. python manage.py startapp app

II.Go to mysite/settings.py: Add "app" to INSTALLED_APPS :
   INSTALLED_APPS = [
    'app',  # new
    .....
   
