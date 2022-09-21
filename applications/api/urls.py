from django.urls import path
from applications.api import helloWorldApiView

urlpatterns = [
    path("api/helloWorld", helloWorldApiView.HelloWorldApiView.as_view()),
]