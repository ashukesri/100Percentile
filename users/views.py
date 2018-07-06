from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST

from .models import (
    Profile,
    UserAnswer,
)
from .serializers import  (
    UserAnswerSerializer,
    ProfileSerializer,
    UserSerializer,
    UserCreateSerialzer,
    #FollowSerializer,
    #UserLoginSerialzer
)

from .permissions import(
    CsrfExemptSessionAuthentication,   
)
from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
)

from rest_framework.permissions import(
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    AllowAny,
)

from rest_framework.authentication import(
    TokenAuthentication,
)

class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerialzer
    permission_classes =  (AllowAny,)
    authentication_classes = (CsrfExemptSessionAuthentication,)
    
    
#class UserLoginAPIView(APIView):
#    permission_class =  [AllowAny]
#    serializer_class = UserLoginSerialzer
#    
#    def post(self, request, *args, **kwargs):
#        data = request.data
#        serializer = UserLoginSerialzer(data=data)
#        if serializer.is_valid(raise_exception=True):
#            new_data=serializer.data
#            return Response(new_data, status = HTTP_200_OK)
#        return Response(serializer.errors,status= HTTP_404_BAD_REQUEST)
    

    
#To see all the users (only admin) (testing purpose only)

#class ProfileListAPIView(ListAPIView):
#    queryset = Profile.objects.all()
#    serializer_class = ProfileSerializer
#    permission_class =  [IsAdminUser]
 
    
class ProfileRetrieveAPIView(RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes =  [IsAuthenticated]
    authentication_classes = (TokenAuthentication, CsrfExemptSessionAuthentication)
    
    

class UserAnswerCreateAPIView(CreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes =  [IsAuthenticated]
    authentication_classes = (TokenAuthentication, CsrfExemptSessionAuthentication)
    
    def perform_create(self,serializer):
        serializer.save(user=self.request.user)
    

class UserAnswerRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_classes =  [IsAdminUser]
    authentication_classes = (TokenAuthentication, CsrfExemptSessionAuthentication)
    


#class FollowCreateAPIView(CreateAPIView):
#    serializer_class = FollowSerializer
#    permission_classes =  [IsAdminUser]
#    
        
