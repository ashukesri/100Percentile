from django.shortcuts import render
#
from . import models #UserProfile
from . import serializers #UserProfileSerializer
from . import permissions
from rest_framework import viewsets,generics,status

from rest_framework.authentication import TokenAuthentication
#
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken

class UserProfileViewSet(viewsets.ModelViewSet):
    serializer_class=serializers.UserProfileSerializer
    queryset= models.UserProfile.objects.all()
    authentication_classes= (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnProfile,)
    
    
class LoginViewSet(viewsets.ViewSet):
    
    serializer_class=AuthTokenSerializer
    
    def create(self, request):
         return ObtainAuthToken().post(request)