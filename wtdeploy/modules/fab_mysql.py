#!/usr/bin/python
# -*- encoding: utf-8 -*-
#
# author: javi santana

from fabric.api import *

def install_mysql():
    """ ripped from http://www.muhuk.com/2010/05/how-to-install-mysql-with-fabric/
    """
    with settings(hide('warnings', 'stderr'), warn_only=True):
        result = sudo('dpkg-query --show mysql-server')
    if result.failed is False:
        warn('MySQL is already installed')
        return
    mysql_password = env.database_admin_pass
    sudo('echo "mysql-server-5.0 mysql-server/root_password password ' \
                              '%s" | debconf-set-selections' % mysql_password)
    sudo('echo "mysql-server-5.0 mysql-server/root_password_again password ' \
                              '%s" | debconf-set-selections' % mysql_password)
    sudo('apt-get install -y  mysql-server')

def install(conf_folder):
   install_mysql()
   sudo("apt-get -y install mysql-client libmysqlclient15-dev") # dev libraries for compile python bindings

def copy_conf_files(conf_folder):
    pass

def create_database(name, encoding='utf8'):
    with settings(warn_only=True):
        run_mysql_sudo('create database %s character set %s' % (name, encoding))

def set_password(user, password):
    sudo("mysqladmin -u %s password %s" % (user, password))

def create_user(user, password):
    run_mysql_sudo("CREATE USER %s IDENTIFIED BY '%s'" % (user, password))

def drop_user(user):
    with settings(warn_only=True):
        run_mysql_sudo("DROP USER %s" % (user))

def user_perms(user, database):
    run_mysql_sudo("grant all on %s.* to %s@'%%'" % (database, user))

def run_mysql_sudo(cmd):
    run('echo "' + cmd + '" | mysql -u%(database_admin)s -p%(database_admin_pass)s' % env)

def get_dump(name, user, password, where):
    # todo make temporally file
    run("mysqldump -u%s -p%s %s | gzip >  /tmp/db_dump.sql.gz" % (user, password, name));
    get("/tmp/db_dump.sql.gz", where)

def drop_database():
    with settings(warn_only=True):
        run_mysql_sudo("DROP DATABASE %s" % env.database_name)

