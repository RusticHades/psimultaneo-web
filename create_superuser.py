import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'psimultaneo.settings')
import django
django.setup()
from django.contrib.auth import get_user_model
User = get_user_model()
User.objects.create_superuser('admin', 'psimultaneo.web@gmail.com', 'GMCA8900g')