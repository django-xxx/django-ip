# -*- coding: utf-8 -*-

from django_six import MiddlewareMixin

from ipaddr.clientip import client_ip


class IPAddrMiddleware(MiddlewareMixin):

    def process_request(self, request):
        request.client_ip = client_ip(request)
        return None
