

Intro
-----
wtdeploy is a toolkit built on top of fabric, that allows you to deploy django applications on ubuntu distribution using apache and mysql

Quick start
-----------

**installing**

    $ pip install -e git+git://github.com/wellnesstelecom/wtdeploy.git#egg=wtdeploy


**project configuration**


configure your django project:
    
- local_settings must be imported at the end of settings file:
        
        from local_settings import *

- put requirements.txt at the same level as settings.py.

** prepare deployment files **

    $ cd myproject
    $ machine_gun init

deploy/localhost folder and a very basic fabfile.py will be created. Edit fabfile.py for more info.

- Edit deploy/localhost/django/local_settings.py if you need, it will be used in the host with this configuration (configuration for each host is selected in fabfile.py)

- check if you need to change deploy/localhost/django/app.wsgi, virtualhost, cron files
    

and finally execute:

    $ fab myhost install
    $ fab myhost deploy

**usage**

First upload changes to your repository

    $ svn commit

deploy the changes

    $ fab myhost deploy



