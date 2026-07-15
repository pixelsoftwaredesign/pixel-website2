import os, django, re
os.environ['DJANGO_SETTINGS_MODULE']='pixel_project.settings'
django.setup()
from django.test import Client
c = Client()
r = c.get('/gestiactiv/dashboard/')
html = r.content.decode('utf-8', errors='replace')
for m in re.findall(r'(?:src|href)=["\']([^"\']+)["\']', html):
    if 'http' in m or 'static' in m or m.startswith('/'):
        print(m)
