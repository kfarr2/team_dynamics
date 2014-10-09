"""
WSGI config for team_dynamics project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/howto/deployment/wsgi/
"""

import os
import site
import sys

prev_sys_path = list(sys.path)
root = os.path.normpath(os.path.join(os.path.dirname(__file__), "../"))
sys.path.append(root)
site.addsitedir(os.path.join(root, ".env/lib/python2.6/site-packages"))

new_sys_path = []
for item in list(sys.path):
    if item not in prev_sys_path:
        new_sys_path.append(item)
        sys.path.remove(item)
sys.path[:0] = new_sys_path

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "td.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
