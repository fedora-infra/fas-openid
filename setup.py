## These two lines are needed to run on EL6
__requires__ = ['SQLAlchemy >= 0.7', 'jinja2 >= 2.4']
import pkg_resources


from setuptools import setup, find_packages

setup(name='FedOAuth',
      version='@VERSION@',
      author='Patrick Uiterwijk',
      author_email='puiterwijk@gmail.com',
      packages=find_packages(),
      zip_safe=False,
      include_package_data=True,
      install_requires=['Flask', 'SQLAlchemy>=0.7',
                        'python-openid', 'flask-sqlalchemy',
                        'flask-babel',
                        'python-openid-teams',
                        'python-openid-cla'])
