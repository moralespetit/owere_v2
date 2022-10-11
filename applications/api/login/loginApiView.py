from rest_framework.generics import GenericAPIView
from rest_framework.response import Response

class loginApiView (GenericAPIView):

    user = ""
    password = ""

    @staticmethod
    def get( request):
        user = request.query_params.get('user')
        password = request.query_params.get('pass')

        return Response({
            'text':'Hola desde el Login !',
            'user': user,
            'password': password
        })
'''
    def get_queryset(self):
        user = self.request.query_params.get('user')
        password = self.request.query_params.get('pass')
'''