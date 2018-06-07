# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView

from .models import BlogPost,BlogImage
from .serializers import BlogPostSerializer, BlogImageSerializer
from .permissions import BlogPostPermission #IsAuthorOrReadOnly     #custom permission
from django.contrib.auth.models import User

from rest_framework.permissions import(
    IsAuthenticated,
#    IsAdminUser,
    IsAuthenticatedOrReadOnly,
    )

class AddPostCreateAPIView(CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_class =  [IsAuthenticated]
    
# views for the Blog post
class BlogPostListAPIView(ListAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_class =  [IsAuthenticated]
    
    
class UserBlogPostListAPIView(ListAPIView):

    serializer_class = BlogPostSerializer
    permission_class =  [IsAuthenticated]
    
    def get_queryset(self):
        return User.objects.get(id=self.request.user.id).BlogPosts.all()

    
class BlogPostRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    permission_class =  (IsAuthenticated,)
#    permission_class =  (BlogPostPermission,)
    
# views for the Blog Image
class BlogImageRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    permission_class =  [IsAuthenticated]
      
        
        
        
        
#class BlogImageCreateAPIView(CreateAPIView):
#    queryset = BlogImage.objects.all()
#    serializer_class = BlogImageSerializer
#    permission_class =  [IsAuthenticated]
    
#class BlogImageListAPIView(ListAPIView):
#    queryset = BlogImage.objects.all()
#    serializer_class = BlogImageSerializer
    

