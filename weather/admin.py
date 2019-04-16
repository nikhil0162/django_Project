from django.contrib import admin
from .models import City




admin.site.register(City)
admin.site.site_header = 'MyAdmin'