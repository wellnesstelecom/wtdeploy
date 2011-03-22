

Intro
-----
wtdeploy is a toolkit built on top of fabric, that allows you to deploy django applications on ubuntu distribution using apache and mysql

Quick start
-----------

**installing**

    $ pip install -e git+git://github.com/wellnesstelecom/wtdeploy.git#egg=wtdeploy


**configuration**

   $ cd myproject
   $ machine_gun init

deploy/localhost and a very basic fabfile.py will be created. Edit fabfile.py for more info

configure your django project:
    
- local_settings must be imported at the end of settings file:
        
        from local_settings import *

in the target machine %(local_conf_folder)s/django/local_settings.py will be used. You can use env variables in your local_settings.py (see example)

- put requirements.txt at the same level as settings.py. If you place requirements.txt in %(local_conf_folder)s/django/ it will be used instead of project requirements.txt

see example/localhost_files to see an example configuration. You can find apache and cron example files

- check if you need to change app.wsgi 
    

and finally execute:

    $ fab myhost install

**usage**

First upload changes to your repository

    $ svn commit

deploy the changes

    $ fab myhost deploy



