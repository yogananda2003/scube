import os
import sys
from django.core.wsgi import get_wsgi_application

# Add the project’s root directory to the Python path
root_path = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, root_path)

# Set the default settings module for Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IWP_PROJECT.settings")

# Get the WSGI application
application = get_wsgi_application()
