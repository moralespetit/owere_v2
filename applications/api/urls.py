from django.urls import path

from applications.api.login.loginApiView import loginApiView
from applications.api.helloworld.helloWorldApiView import helloWorldApiView
from applications.api.client.clientApiView import *

urlpatterns = [
    path("api/helloworld",  helloWorldApiView.as_view()),
    path("api/clients/", clientListApiView.as_view()),
    path("api/client", clientCreateApiView.as_view()),
    path("api/login", loginApiView.as_view()),

]