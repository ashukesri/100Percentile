# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from rest_framework.generics import CreateAPIView,ListCreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from django.contrib.auth.models import User
from django.db.models import Q

from .models import (
    Topic,
    SubTopic,
    Question,
    QuestionImage,
    QuestionOption,
    QuestionSolution,
    QuestionDiscussion,
)

from .serializers import (
    TopicSerializer,
    SubTopicSerializer,
    QuestionSerializer,
    QuestionImageSerializer,
    QuestionOptionSerializer,
    QuestionSolutionSerializer,
    QuestionDiscussionSerializer,
    )

from rest_framework.permissions import(
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )
##########################################################################

class TopicCreateAPIView(CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes =  [IsAdminUser]
    
class TopicRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_classes =  [IsAdminUser,IsAuthenticatedOrReadOnly]
    
##########################################################################
class QuestionSolutionCreateAPIView(ListCreateAPIView):
    queryset = QuestionSolution.objects.all()
    serializer_class = QuestionSolutionSerializer
    permission_classes =  [IsAdminUser]
    
class QuestionSolutionRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionSolution.objects.all()
    serializer_class = QuestionSolutionSerializer
    permission_classes =  [IsAdminUser,IsAuthenticatedOrReadOnly]

    
##########################################################################

class QuestionDiscussionCreateAPIView(ListCreateAPIView):
    queryset = QuestionDiscussion.objects.all()
    serializer_class = QuestionDiscussionSerializer
    permission_classes =  [IsAuthenticated]
    
class QuestionDiscussionRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionDiscussion.objects.all()
    serializer_class = QuestionDiscussionSerializer
    permission_classes =  [IsAuthenticatedOrReadOnly]

    
##########################################################################

class SubTopicCreateAPIView(CreateAPIView):
    queryset = SubTopic.objects.all()
    serializer_class = SubTopicSerializer
    permission_classes =  [IsAuthenticated]
    
class SubTopicRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubTopic.objects.all()
    serializer_class = SubTopicSerializer
    permission_classes =  [IsAuthenticatedOrReadOnly]


##########################################################################
# views for the Question 

class AddQuestionCreateAPIView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes =  [IsAuthenticated]
    def perform_create(self,serializer):
        serializer.save(author=self.request.user) 
        

class QuestionListAPIView(ListAPIView):
    serializer_class = QuestionSerializer
    permission_classes =  [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.GET.get('user'):   #accessed by ?user=3 format
            return Question.objects.filter(author=self.request.GET.get('user'))               
        elif self.request.user.is_authenticated() and self.request.user.profile.is_subscribed:
            return Question.objects.filter(status=4)
        else:
            return Question.objects.filter(is_subscribed=False).filter(status=4)

        
# use will see the question which he can edit eg. The posts which are pending to be reviewed by the reviewer
class UserQuestionListAPIView(ListAPIView):
    
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated,]
    def get_queryset(self):
        if self.request.user.profile.role=='4':
            return Question.objects.filter(author=self.request.user)
        elif self.request.user.profile.role=='3':
            return Question.objects.filter(status=1)    # .filter(status=3)
        elif self.request.user.profile.role=='2':
            print("user entered")
            return Question.objects.filter(Q(status=3)| Q(status=4))
        else:
            return Question.objects.all()
    
class QuestionRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes =  [IsAuthenticated]
    

##########################################################################
# views for the Quesion Image

class QuestionImageRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionImage.objects.all()
    serializer_class = QuestionImageSerializer
    permission_classes =  [IsAuthenticated]
    
    
##########################################################################
# views for the Quesion Answer
   
class QuestionOptionCreateAPIView(CreateAPIView):
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionSerializer
    permission_classes =  [IsAuthenticated]


class QuestionOptionRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionOption.objects.all()
    serializer_class = QuestionOptionSerializer
    permission_classes =  [IsAuthenticated]
    