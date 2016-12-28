=========
django-IP
=========

Simple return user's real IP address in Django

Installation
============

::

    pip install django-ip


Usage
=====

::

    # Need Setting
    request.client_ip

    # Not Need Setting
    from ipaadr import client_ip
    def xxx(request):
        ipaddr = client_ip(request)


Settings.py
===========

::

    # Use `MIDDLEWARE_CLASSES` prior to Django 1.10
    MIDDLEWARE = (
        ...
        'ipaddr.middleware.IPAddrMiddleware',
        ...
    )

