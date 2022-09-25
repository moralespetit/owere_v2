from django.urls import path, include, re_path

from django.contrib import admin

admin.autodiscover()

import hello.views

# To add a new path, first import the app:
# import blog
#
# Then add the new path:
# path('blog/', blog.urls, name="blog")
#
# Learn more here: https://docs.djangoproject.com/en/2.1/topics/http/urls/

urlpatterns = [
    path("", hello.views.index, name="index"),
    path("db/", hello.views.db, name="db"),
    path("admin/", admin.site.urls),
    re_path('', include('applications.api.urls')),

]

'''
from django.db import connections
from django.db.utils import OperationalError
conn = connections['heroku-potsgres']
try:
    c = conn.cursor() #this will take some time if error
    c.execute('select * from test_public')
    row = c.fetchone()
    print(row)
except OperationalError:
    reachable = False
else:
    reachable = True

print(reachable)
'''