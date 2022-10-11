#from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from rest_framework.response import Response
#from .serializers import TestSerializer
from applications.model.client import *


class clientListApiView(ListAPIView):

    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()


class clientCreateApiView(CreateAPIView):

    serializer_class = ClientSerializer





