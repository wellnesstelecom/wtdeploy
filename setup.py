from distutils.core import setup

setup(name='wtdeploy', 
      author = 'Javi Santana', 
      author_email = 'jsantana@wtelecom.es',
      description = 'django projects deploy on ubuntu',
      version='0.1',
      packages=['wtdeploy'],
      requires = ['fabric']
)
