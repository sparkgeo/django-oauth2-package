#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages


import os

here = os.path.dirname(os.path.abspath(__file__))
f = open(os.path.join(here, 'README'))
long_description = f.read().strip()
f.close()


setup(
    name='django-oauth2-package',
    version='0.3.0',
    author='Sparkgeo',
    author_email='dustin@sparkgeo.com',
    url='https://github.com/sparkgeo/django-oauth2-package',
    description='',
    packages=find_packages(),
    long_description=long_description,
    keywords='',
    zip_safe=False,
    install_requires=[
        'Django>=1.8.0',
        'djangorestframework>=3.0',
        'django-oauth-toolkit==0.11',
        'django-cors-middleware==1.3.1',
    ],
    include_package_data=True,
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ],
)
