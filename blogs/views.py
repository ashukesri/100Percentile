# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework.generics import CreateAPIView, RetrieveUpdateDestroyAPIView, ListAPIView, RetrieveAPIView
from rest_framework.views import APIView

from .models import BlogPosts,BlogImage
from .serializers import BlogPostAndImageSerializer, BlogPostsSerializer, BlogImageSerializer
from .permissions import IsAuthorOrReadOnly

from rest_framework.permissions import(
    IsAuthenticated,
#    IsAdminUser,
#    IsAuthenticatedOrReadOnly,
    )


class AddPostCreateAPIView(CreateAPIView):
    queryset = BlogPosts.objects.all()
    serializer_class = BlogPostAndImageSerializer
    permission_class =  [IsAuthenticated]
    
# views for the Blog post
class BlogPostListAPIView(ListAPIView):
    queryset = BlogPosts.objects.all()
    serializer_class = BlogPostsSerializer
    

class BlogPostRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogPosts.objects.all()
    serializer_class = BlogPostsSerializer
    permission_class =  [IsAuthenticated]
    
# views for the Blog Image
    
class BlogImageCreateAPIView(CreateAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    permission_class =  [IsAuthenticated]
    
class BlogImageListAPIView(ListAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    
class BlogImageRUDAPIView(RetrieveUpdateDestroyAPIView):
    queryset = BlogImage.objects.all()
    serializer_class = BlogImageSerializer
    permission_class =  [IsAuthenticated]
    

    
#class BlogPostCreateAPIView(CreateAPIView):
#    queryset = BlogPosts.objects.all()
#    serializer_class = BlogPostsSerializer
#    permission_class =  [IsAuthenticated]
#    
#    def perform_create(self, serializer):
#        serializer.save(author = self.request.UserProfile)
