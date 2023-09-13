# Pigeon Clocking System
A simple Django application for pigeon race clocking.


# Installation (Ubuntu 22)
The following steps were taken from https://www.youtube.com/watch?v=7O1H9kr1CsA&ab_channel=CloudWithDjango but was implemented in Raspberry Pi 4 with Ubuntu 22 Server (64-bit) and a public IP address.
1. Update and upgrade your server.
> sudo apt-get update  
> sudo apt-get upgrade
2. Install a virtual environment.  
> sudo apt-get install python3-venv  
3. Create a virtual environment with a name 'env'. You can replace it whatever you like.  
> python3 -m venv env
4. Enable the virtual environment.  
> source env/bin/activate  
The line in the terminal console should look like this:  
> (env)user@ubuntu:~$
5. Install Django, make sure that you choose the version which is the same or compatible with your project's Django version. 
> pip install Django
6. Clone your repository.  Cloning repository in GitHub creates a local directory in your machine with a directory name equal to your 
repository name.  It is recommended to manage your repository's file hierarchy similar to this project.  Also, a reminder that cloning in GitHub private repository will ask for username and password. Password cannot be used instead use token generated from developer settings in you GitHub account. 
> git clone https://github.com/choloxs/clickclock.git  
7. Install Nginx  
> sudo apt-get install -y nginx
8. Install gunicorn  
> pip install gunicorn
9. Test nginx by typing your host IP address or your server name.  
10. Install supervisor.  Please watch the video for more information about this supervisor.  
> sudo apt-get install supervisor  
11. Go to /etc/supervisor/conf.d/ directory with the following line.  
> cd /etc/supervisor/conf.d/
12. Create a config file named gunicorn.conf  
> sudo touch gunicorn.conf
13. Edit gunicorn.conf file.  Please refer to the content of gunicorn.conf file provided in this repository or you can move the file in repository to the /etc/supervisor/conf.d/ directory. The 'user' and 'projectname' in the content should be replaced with your user and project names.
> sudo nano gunicorn.conf
14. Create the following directory for gunicorn logs.  
> sudo mkdir /var/log/gunicorn
15. Run the following lines 
> sudo supervisorctl reread   

result to 'available'
> sudo supervisorctl update  

result to 'added process group'
> sudo supervisorctl status

result to 'RUNNING'


16. Go to the /etc/nginx directory.   
> cd ..  
> cd ..
> cd nginx
17. Edit the nginx.conf file.  Replace the first line with 'user root;'
> sudo nano nginx.conf
18. Move to /etc/nginx/sites-available/ directory.  
> cd sites-available
19. Create django.conf file.  
> sudo touch django.conf
20. Edit the django.conf file.  This file is the configuration file for you server.  The file is provided in this repository, please check the comments in the content.
> sudo nano django.conf
21. Perform test on nginx.
> sudo nginx -t
22. Create a symbolic link between the enabled-sites and sites-available.
> sudo ln django.conf /etc/nginx/sites-enabled

or if you are on the home directory

> sudo ln /etc/nginx/sites-available/django.conf /etc/nginx/sites-enabled
23. Remove or comment all the fields in /etc/nginx/sites-available/default.  Removing the file also works for me.
* Comment all fields with '#'
> sudo nano /etc/nginx/sites-available/default
* Remove the file from sites-available and sites-enabled
> rm /etc/nginx/sites-available/default
> rm /etc/nginx/sites-enabled/default
24. Configure your Django.  In settings.py edit the following lines with your configurations.
> ALLOWED HOSTS
> DEBUG=False

If you are planning to use the Django admin, it's better to set up your settings.py with this, this is also reflected in django.conf file in /etc/nginx/sites-available/
> import os
> STATIC_URL = '/static/'
> STATIC_ROOT = os.path.join(BASE_DIR, 'static')

Then go to your project directory
> cd
> cd projectdirectory

Run the following commands:
* To merge the default Django static files with the base directory.
> python manage.py collectstatic

* In this case the sqlite database is not included in the repository.
> python manage.py makemigrations  
> python manage.py migrate
> python manage.py createsuperuser

25. Restart your nginx.
>sudo service nginx restart

# To update application from GitHub
1. Activate your virtual environment
> source env/bin/activate
2. Go to project directory from home directory.
> cd projectdirectory
3. Save the current git repository in your local machine.
> git stash
4. Pull the updated repository in your GitHub. This will require login for private repository
> git pull
5. Restart your nginx.
>sudo service nginx restart
6. If no changes was observed,l then reboot your local machine.
> sudo reboot
