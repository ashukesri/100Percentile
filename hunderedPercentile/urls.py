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
from django.contrib import admin

from blogs.views import(AddPostCreateAPIView,
                        BlogImageCreateAPIView,
                        BlogImageListAPIView,
                        BlogImageRUDAPIView,
                        BlogPostRUDAPIView,
                        BlogPostListAPIView,)
                         
from questions.views import(AddQuestionCreateAPIView,
                        QuestionListAPIView,
                        QuestionRUDAPIView,
                        QuestionImageCreateAPIView,
                        QuestionImageListAPIView,
                        QuestionImageRUDAPIView,
                        TopicCreateAPIView
                        TopicRUDAPIView,
                        SubTopicCreateAPIView,
                        SubTopicRUDAPIView,
                        )
                    
                    
urlpatterns = [
    url(r'^blog/posts$'                     ,BlogPostListAPIView.as_view()     ,name="posts"),
    url(r'blog/post-add'                    ,AddPostCreateAPIView.as_view()    ,name="post_create"),
    url(r'blog/post-edit/(?P<pk>\d+)/'      ,BlogPostRUDAPIView.as_view()      ,name="post_edit"),
    url(r'^blog/post-images$'                ,BlogImageListAPIView.as_view()    ,name="post_image"),
    url(r'blog/post-add-image'              ,BlogImageCreateAPIView.as_view()  ,name="post_add_image"),
    url(r'blog/post-edit-image/(?P<pk>\d+)/',BlogImageRUDAPIView.as_view()     ,name="post_edit_image"),
    
    url(r'^question/questions$'                     ,QuestionListAPIView.as_view()         ,name="questions"),
    url(r'question/question-create'                 ,AddQuestionCreateAPIView.as_view()    ,name="question_create"),
    url(r'question/question-edit/(?P<pk>\d+)/'      ,QuestionRUDAPIView.as_view()          ,name="question_edit"),
#    url(r'^question/post-image$'                     ,QuestionImageListAPIView.as_view()    ,name="question_image"),
    url(r'question/question-add-image'              ,QuestionImageCreateAPIView.as_view()  ,name="question_add_image"),
    url(r'question/question-edit-image/(?P<pk>\d+)/',QuestionImageRUDAPIView.as_view()     ,name="question_edit_image"),  
    
    url(r'^admin/'      , admin.site.urls),
]
