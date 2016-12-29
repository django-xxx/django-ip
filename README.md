# django-ip
Simple return user's real IP address in Django

## django-uri

* Installation

  ```shell
  pip install django-ip
  ```

* Settings.py

  ```python
  # Use `MIDDLEWARE_CLASSES` prior to Django 1.10
  MIDDLEWARE = (
    ...
    'ipaddr.middleware.IPAddrMiddleware',
    ...
  )
  ```

* Usage

  ```python
  # Need Setting
  request.client_ip

  # Not Need Setting
  from ipaddr import client_ip
  def xxx(request):
      ipaddr = client_ip(request)
  ```
