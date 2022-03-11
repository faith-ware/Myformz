from xmlrpc.client import ResponseError
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class CollectForm(APIView):
    authentication_classes = [BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response({"Hello" : "There"})

    def post(self, request, format=None):
        print(request.data)
        print(request.user.email)
        return Response({"Yo" : "Recieved"})