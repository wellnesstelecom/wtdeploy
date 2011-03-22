from distutils.core import setup
import os
from os.path import join


def get_data_files(path):
    total_files = []
    for root, dirs, files in os.walk(path):
        total_files += [join(root, name).split('/',1)[1] for name in files]
    return total_files


setup(name='wtdeploy', 
      author = 'Javi Santana', 
      author_email = 'jsantana@wtelecom.es',
      description = 'django projects deploy on ubuntu',
      url='https://github.com/wellnesstelecom/wtdeploy',
      version='0.3',
      packages=['wtdeploy', 'wtdeploy.modules'],
      scripts=['machine_gun'],
      requires = ['fabric'],
      package_data={'wtdeploy': ['fabfile.py.template'] + get_data_files('wtdeploy/base_template')}
)
