from django.contrib import admin
from applications.model.company import Company
from applications.model.client import Client
# Register your models here.

admin.site.register(Company)
admin.site.register(Client)
