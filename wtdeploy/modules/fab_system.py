#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: Alvaro Lazaro

from fabric.api import *

def create_user(name, group, password):
    # crypting the pass
    crypt_pass = local("mkpasswd -m SHA-512 '%s'" % password)
    with settings(warn_only=True):
        create_group(group)
    sudo("useradd -m -b /home -s /bin/bash -g '%s' -p '%s' '%s'" % (group, crypt_pass[:-1], name))

def remove_user(name):
    sudo("userdel '%s'" % name)

def create_group(name):
    sudo("groupadd '%s'" % name)

def remove_group(name):
    sudo("groupdel '%s'" % name)
