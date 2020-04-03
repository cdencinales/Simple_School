from rest_framework import status
from rest_framework import response
from rest_framework.decorators import api_view
from account.api.serializers import RegistrationSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from account.api.serializers import RegistrationSerializer
from account import models


@api_view(['POST',])

def registration_view(request):
    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data) 
        data = {}
        if serializer.valid():
            account = serializer.save()
            data['response'] = 'Succesfuly registered a new user.'
            data['email'] = account.email
            data['username'] = account.username
        else:
            data = serializer.errors
        return Response(data)
    
    authentication_classes = [TokenAuthentication, SessionAuthentication, BasicAuthentication]
    permission_clases = [IsAuthenticated]

class AccountViewSet(viewsets.ModelViewSet):
    queryset = models.Account.objects.all()
    serializer_class = RegistrationSerializer