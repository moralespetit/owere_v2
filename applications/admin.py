from django.contrib import admin
from applications.model.company import Company
from applications.model.client import Client
from applications.admins.adminCustomize import *
# Register your models here.

admin.site.register(Company, CompanyAdmin)
admin.site.register(Client, ClientAdmin)

