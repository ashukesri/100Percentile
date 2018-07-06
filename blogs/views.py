# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt

from rest_framework.generics import(
    CreateAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView, 
    ListAPIView, 
    RetrieveAPIView,
)
from django.db.models import Q
from .models import (
    BlogPost,
    BlogImage,
    BlogPostDiscussion,
)
from .serializers import (
    BlogPostSerializer,
    BlogImageSerializer,
    BlogPostDiscussionSerializer,
)
from .permissions import (
    BlogPostListPermission,
    BlogPostPermission,
    CsrfExemptSessionAuthentication,
)
from django.contrib.auth.models import User
from rest_framework import serializers

from rest_framework.authentication import(
    SessionAuthentication, 
    BasicAuthentication,
    TokenAuthentication,
)
from rest_framework.permissions import(
    IsAuthenticated,
    AllowAny,
#    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

#########################################################################

class AddPostCreateAPIView(CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes =  [IsAuthenticated]
#    authentication_classes = (SessionAuthentication, BasicAuthentication,CsrfExemptSessionAuthentication)
    authentication_classes = (TokenAuthentication, CsrfExemptSessionAuthentication)
    
    def perform_create(self,serializer):
        serializer.save(author=self.request.user)
    
# views for the Blog post

class BlogPostListAPIView(ListAPIView):
    serializer_class = BlogPostSerializer
    permission_classes =  (BlogPostListPermission,)
    authentication_classes = (TokenAuthentication, CsrfExemptSessionAuthentication)
    
    
    def get_queryset(self):
        if self.request.GET.get('user'):
            return BlogPost.objects.filter(author=self.request.GET.get('user'))
        else:
            return BlogPost.objects.filter(status=4)

# use will see the posted which he can edit eg. The posts which are pending to be reviewed by the reviewer

class UserBlogPostListAPIView(ListAPIView):
    
    serializer_class = BlogPostSerializer
    permission_classes = [IsAuthenticated,]
    authentication_classes = (TokenAuthentication, CsrfExemptSessionAuthentication)
    
    def get_queryset(self):
        if self.request.user.profile.role=='4':
            return BlogPost.objects.filter(author=self.request.user)
        elif self.request.user.profile.role=='3':
            return BlogPost.objects.filter(status=1)    # .filter(status=3)
        elif self.request.user.profile.role=='2':
            return BlogPost.objects.filter(Q(status=3)| Q(status=4))
        else:
            return BlogPost.objects.all()
        
##########################################################################

class BlogPostDiscussionCreateAPIView(ListCreateAPIView):
    queryset = BlogPostDiscussion.objects.all()
    serializer_class = BlogPostDiscussionSerializer
    permission_classes =  [IsAuthenticated]
    authentication_classes = (TokenAuthentication, CsrfExemptSessionAuthentication)
    


class BlogPostDiscussionRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPostDiscussion.objects.all()
    serializer_class = BlogPostDiscussionSerializer
    permission_classes =  [IsAuthenticatedOrReadOnly]
    authentication_classes = (TokenAuthentication, CsrfExemptSessionAuthentication)
    

    
##########################################################################

class BlogPostRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_classes =  (BlogPostPermission,)
    authentication_classes = (TokenAuthentication, CsrfExemptSessionAuthentication)
    
    
# views for the Blog Image

class BlogImageRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    permission_classes =  [IsAuthenticated]
    authentication_classes = (TokenAuthentication, CsrfExemptSessionAuthentication)
    
    
    
#class BlogImageCreateAPIView(CreateAPIView):
#    queryset = BlogImage.objects.all()
#    serializer_class = BlogImageSerializer
#    permission_classes =  [IsAuthenticated]

   
#class BlogImageListAPIView(ListAPIView):
#    queryset = BlogImage.objects.all()
#    serializer_class = BlogImageSerializer
    

#class UserBlogPostListAPIView(ListAPIView):
#
#    serializer_class = BlogPostSerializer
#    permission_classes =  [IsAuthenticated]
#    
#    def get_queryset(self):
#        return User.objects.get(id=self.request.user.id).BlogPosts.all()
