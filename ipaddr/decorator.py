# -*- coding: utf-8 -*-

from functools import wraps

from django.http import HttpResponseForbidden
from ipaddr.clientip import client_ip


def check_ip(func=None, ip=None):
    def decorator(func):
        @wraps(func)
        def legal_ip(request, *args, **kwargs):
            if ip and client_ip(request) not in ip:
                return HttpResponseForbidden()
            return func(request, *args, **kwargs)
        return legal_ip

    if not func:
        def decorator2(func):
            return decorator(func)
        return decorator2

    return decorator(func)
