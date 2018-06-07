# -*- coding: utf-8 -*-
from __future__ import unicode_literals

#from django.shortcuts import render

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView

from .models import Topic,SubTopic,Question,QuestionImage,QuestionAnswer
from .serializers import TopicSerializer, SubTopicSerializer, QuestionSerializer, QuestionImageSerializer, QuestionAnswerSerializer

from rest_framework.permissions import(
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

class TopicCreateAPIView(CreateAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_class =  [IsAuthenticated]
    

class TopicRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Topic.objects.all()
    serializer_class = TopicSerializer
    permission_class =  [IsAdminUser,IsAuthenticatedOrReadOnly]

    
class SubTopicCreateAPIView(CreateAPIView):
    queryset = SubTopic.objects.all()
    serializer_class = SubTopicSerializer
    permission_class =  [IsAuthenticated]
    

class SubTopicRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = SubTopic.objects.all()
    serializer_class = SubTopicSerializer
    permission_class =  [IsAdminUser,IsAuthenticatedOrReadOnly]



    
# views for the Question 

class AddQuestionCreateAPIView(CreateAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class =  [IsAuthenticated]
    

class QuestionListAPIView(ListAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class =  [IsAuthenticated]

    
class QuestionRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_class =  [IsAuthenticated]
    
    
# views for the Quesion Image
class QuestionImageRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionImage.objects.all()
    serializer_class = QuestionImageSerializer
    permission_class =  [IsAuthenticated]
    
# views for the Quesion Answer
   
class QuestionAnswerCreateAPIView(CreateAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    permission_class =  [IsAuthenticated]


class QuestionAnswerRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer
    permission_class =  [IsAuthenticated]
    