# django-ip
Simple return user's real IP address in Django

## Installation
```shell
pip install django-ip
```

## Usage
```python
# Need Setting
request.client_ip

# Not Need Setting
from ipaddr import client_ip
def xxx(request):
    ipaddr = client_ip(request)
```

## Settings.py
```python
# Use `MIDDLEWARE_CLASSES` prior to Django 1.10
MIDDLEWARE = (
    ...
    'ipaddr.middleware.IPAddrMiddleware',
    ...
)
```
