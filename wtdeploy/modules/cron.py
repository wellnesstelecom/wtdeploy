#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: javi santana

from fabric.api import *
from fabric.contrib.files import upload_template
from fabric.contrib.files import exists

def copy_conf_files(conf_folder, deploy_folder):
    cron_filename = 'wtdeploy_%s' % env.host.replace('.','_');
    upload_template('%s/cron/tasks' % conf_folder, deploy_folder, context=env)
    sudo('cp %s/tasks /etc/cron.d/%s' % (deploy_folder, cron_filename))
    sudo('chmod +r /etc/cron.d/%s' % cron_filename)
