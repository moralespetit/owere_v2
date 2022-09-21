from rest_framework.generics import ListAPIView
from .serializers import TestSerializer


class HelloWorldApiView(ListAPIView):
    serializer_class = TestSerializer

    def get_queryset(self):
        return {"message": "Hello World!"}
