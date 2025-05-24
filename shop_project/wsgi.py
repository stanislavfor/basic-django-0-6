import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project directory to the sys.path
path = '/home/stass/basic-django-0-6'
if path not in sys.path:
    sys.path.append(path)

# Set the DJANGO_SETTINGS_MODULE environment variable
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shop_project.settings')

application = get_wsgi_application()
