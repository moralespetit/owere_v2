#from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
#from .serializers import TestSerializer


class helloWorldApiView(GenericAPIView):
    #serializer_class = TestSerializer

    @staticmethod
    def get(request):

        print(" ------ helloWorldApiView.get ------ ")
        return Response({'text': 'Hello World!'})

    #def get_queryset(self):
    #    return {"message": "Hello World!"}