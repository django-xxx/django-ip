# -*- coding: utf-8 -*-

from setuptools import setup


version = '1.0.0'


setup(
    name='django-ip',
    version=version,
    keywords='django-ip',
    description='Django Client IP',
    long_description=open('README.rst').read(),

    url='https://github.com/django-xxx/django-ip',

    author='Hackathon',
    author_email='kimi.huang@brightcells.com',

    packages=['ipaddr'],
    py_modules=[],
    install_requires=['django-six'],

    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Office/Business :: Financial :: Spreadsheet',
    ],
)
