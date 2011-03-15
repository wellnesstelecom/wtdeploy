

Intro
-----
wtdeploy is a toolkit on top of fabric to deploy django applications on ubuntu distribution using apache and mysql

Quick start
-----------

**installing**

    $ pip install wtdeploy

**configuration**

create your fabfile as usual:

    # fabfile.py
 
    from wtdeploy import install, deploy
    # you can import other task like backup, quick_deploy, see tasks.py for more task

    def myhost():

      # host configuration, hostname and user/pass
      env.hosts = ['localhost']
      env.user = 'deploybot' # must be created previously
      env.password = 'password' 
      env.local_conf_folder = "deploy/localhost" # path where host configuraton is placed
                                                 # see example/localhost_files

      # database
      env.database_admin = 'root' # user will be created on install task
      env.database_admin_pass = 'root' 
      env.database_user = 'user' # user will be created too
      env.database_pass = 'pass'
      env.database_name = 'database' # database is created during install

      # svn 
      env.repo_user = env.user
      env.repo_password = env.password
      env.repo =  "https://svn/project/trunk/" # path where app is placed (manage.py, urls.py...)

      # where to put files
      env.deploy_folder = "/home/deploybot/project"
      env.is_mobile = False

      # put here new tasks!!

configure your django project:
    
- at the end of settings file must be imported local_settings:
        
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



