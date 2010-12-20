#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: javi santana

from fabric.api import *
from fabric.contrib.files import upload_template
from fabric.contrib.files import exists


def install(conf_folder):
   sudo("apt-get -y install apache2 libapache2-mod-wsgi")
   #sudo("rm -rf /etc/apache2/site-enabled/*")

def copy_conf_files(conf_folder, deploy_folder):
  with cd(deploy_folder):
    run('mkdir -p apache2')
    #put('%s/apache/virtualhost' % conf_folder, 'apache2')
    if env.is_mobile:
        print "mobile template"
        upload_template('%s/apache/virtualhost_mobile' % conf_folder, 'apache2/virtualhost', context=env)
    else:
        upload_template('%s/apache/virtualhost' % conf_folder, 'apache2', context=env)
    sudo('cp apache2/virtualhost /etc/apache2/sites-available/%(host)s' % env)
    sudo('chmod a+r /etc/apache2/sites-available/%(host)s' % env)
    if not exists('/etc/apache2/sites-enabled/00-%(host)s' % env):
      sudo('ln -s /etc/apache2/sites-available/%(host)s /etc/apache2/sites-enabled/00-%(host)s' % env)

def start():
  sudo("/etc/init.d/apache2 start")

def stop():
  sudo("/etc/init.d/apache2 stop")

def restart():
  sudo("/etc/init.d/apache2 restart")
