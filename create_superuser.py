# create_superuser.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'psimultaneo.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='PsimultaneoAdmin').exists():
    User.objects.create_superuser('PsimultaneoAdmin', 'psimultaneo.web@gmail.com', 'GMCA8900g')
    print("Superusuario creado!")
else:
    print("El superusuario ya existe.")