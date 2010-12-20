#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: javi santana

from fabric.api import *


# Tasks

def install(conf_folder):
   install_prereqs()

def install_prereqs():
   sudo("apt-get -y install munin-node chkconfig")
   sudo("chkconfig munin-node on")

def copy_conf_files(conf_folder):
   run('mkdir -p munin')
   put('%s/munin/munin-node.conf' % conf_folder, 'munin')
   put('%s/munin/munin-node' % conf_folder, 'munin')
   sudo('cp munin/munin-node.conf /etc/munin/')
   sudo('cp munin/munin-node /etc/munin/plugin-conf.d')

def start():
   sudo('service munin-node start')

def stop():
   sudo('service munin-node stop')

def restart():
   sudo('service munin-node restart')
