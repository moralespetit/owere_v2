from django.urls import path
from applications.api.helloworld.helloWorldApiView import helloWorldApiView

urlpatterns = [
    path("api/helloworld",  helloWorldApiView.as_view()),
]