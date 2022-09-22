from django.urls import path
from applications.api.helloworld import helloWorldApiView

urlpatterns = [
    path("api/helloworld", helloWorldApiView.HelloWorldApiView.as_view()),
]