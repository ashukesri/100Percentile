from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Profile, UserAnswer
from .serializers import ProfileSerializer, UserAnswerSerializer
from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import(
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
#def update_profile(request, user_id):
#    user = User.objects.get(pk=user_id)
#    user.save()

class UserAnswerCreateAPIView(CreateAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_class =  [IsAuthenticated]
    

class UserAnswerRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = UserAnswer.objects.all()
    serializer_class = UserAnswerSerializer
    permission_class =  [IsAdminUser,IsAuthenticatedOrReadOnly]
