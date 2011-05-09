!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: flopezluis

from fabric.api import *
from fabric.contrib.files import upload_template
from fabric.contrib.files import exists


def install(conf_folder):
    sudo("pip install supervisor")

def copy_conf_files(conf_folder, deploy_folder):
    sudo("rm -rf /etc/supervisord.conf" % env)
    sudo("ln -s %(deploy_folder)s/app/deploy/supervisord.conf /etc/supervisord.conf" % env)

def reload(services):
    """ restart services """
    # start supervisord
    with settings(warn_only=True):
        sudo("supervisord")
    sudo("supervisorctl reload") # reload supervisor conf
    for service in services:
        sudo("supervisorctl restart %s" %service)
