"""hunderedPercentile URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from .views import( AddPostCreateAPIView,
                    BlogImageRUDAPIView,
                    BlogPostRUDAPIView,
                    BlogPostListAPIView,
                    UserBlogPostListAPIView,
#                    BlogImageCreateAPIView,
#                    BlogImageListAPIView,                  
                  )
                         
                    
                    
urlpatterns = [
    url(r'^$'                          ,BlogPostListAPIView.as_view()     ,name="posts"),
    url(r'user'                        ,UserBlogPostListAPIView.as_view()    ,name="user_post"),
    url(r'post-add'                    ,AddPostCreateAPIView.as_view()    ,name="post_create"),
    url(r'post-edit/(?P<pk>\d+)/'      ,BlogPostRUDAPIView.as_view()      ,name="post_edit"),
    url(r'post-edit-image/(?P<pk>\d+)/',BlogImageRUDAPIView.as_view()     ,name="post_edit_image"),
#    url(r'^post-images$'                ,BlogImageListAPIView.as_view()    ,name="post_image"),
#    url(r'post-add-image'              ,BlogImageCreateAPIView.as_view()  ,name="post_add_image"),
]
