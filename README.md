# django_personal_homepage
personal homepage made in django, all changes are done through django admin

install python-dotenv, pillow (for images), mysqlclient (or whatever db you use)

py manage.py makemigrations  
py manage.py migrate  
py manage.py createsuperuser  

db variables in settings.py are managed
with python-dotenv and an .env file (gitignored for safety)
stored in the root folder
