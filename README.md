# clickclock
A simple Django application for pigeon race clocking.


# Installation (Ubuntu 22)
1. sudo apt-get update
2. sudo apt-get upgrade
3. sudo apt-get install python3-venv //install virtual environment
4. python3 -m venv env //create virtual environment
5. source env/bin/activate //enable virtual environment
6. pip install Django //install django
7. git clone https://github.com/choloxs/clickclock.git
8. sudo apt-get install -y nginx
9. pip install gunicorn
10. Test nginx by typing the host IP address
11. sudo apt-get install supervisor
12. cd /etc/supervisor/conf.d/
13. sudo touch gunicorn.conf
14. sudo nano gunicorn.conf
15. sudo mkdir /var/log/gunicorn
16. sudo supervisorctl reread //result 'available'
17. sudo supervisorctl update //result 'added process group'
18. sudo supervisorctl status //result 'RUNNING'
19. cd ..
20. cd ..
21. cd nginx
22. sudo nano nginx.conf
23. edit user 'user root;'
24. cd sites-available
25. sudo touch django.conf
26. sudo nano django.conf
27. sudo nginx -t
28. sudo ln django.conf /etc/nginx/sites-enabled ##copy to nginx default if does not work: sudo nano /etc/nginx/sites-available/default
29. sudo service nginx restart
30. certbot
31. Configure django settings
In settings.py:
add header line 'import os'
edit the ALLOWED HOSTS
set DEBUG=False
edit the STATIC line with:
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

    
> python manage.py collectstatic
python manage.py createsuperuser
python manage.py makemigrations
python manage.py migrate

32. insert the following line in sites-available/default
    location /static/ {
        alias /home/user/projectname/static/;
    }

34. sudo service nginx restart

# To update application from github
source env/bin/activate //enable virtual environment
git clone https://github.com/choloxs/clickclock.git
run migrations

#       Code