from django.conf.urls import url
                       
from .views import(     AddQuestionCreateAPIView,
                        QuestionListAPIView,
                        QuestionRUDAPIView,
                        QuestionImageRUDAPIView,
                        UserQuestionListAPIView,
                   
                        TopicCreateAPIView,
                        TopicRUDAPIView,
                        SubTopicCreateAPIView,
                        SubTopicRUDAPIView,
                   
                        QuestionOptionCreateAPIView,
                        QuestionOptionRUDAPIView,
                        )
                    
                    
urlpatterns = [
    
    url(r'^$'                              ,QuestionListAPIView.as_view()         ,name="questions"),
    url(r'user'                             ,UserQuestionListAPIView.as_view()    ,name="user_questions"),
    url(r'question-create'                 ,AddQuestionCreateAPIView.as_view()    ,name="question_create"),
    url(r'question-edit/(?P<pk>\d+)'      ,QuestionRUDAPIView.as_view()          ,name="question_edit"),
    url(r'question-edit-image/(?P<pk>\d+)',QuestionImageRUDAPIView.as_view()     ,name="question_edit_image"),  
    
    url(r'option-create'                   ,QuestionOptionCreateAPIView.as_view() ,name="question_answer_create"),
    url(r'option-edit/(?P<pk>\d+)'        ,QuestionOptionRUDAPIView.as_view()    ,name="question_answer_edit"),
    
    
    url(r'topic-create'                    ,AddQuestionCreateAPIView.as_view()    ,name="topic_create"),
    url(r'topic-edit/(?P<pk>\d+)'         ,QuestionRUDAPIView.as_view()          ,name="topic_edit"),
     
    url(r'subTopic-create'                 ,AddQuestionCreateAPIView.as_view()    ,name="subTopic_create"),
    url(r'subTopic-edit/(?P<pk>\d+)'      ,QuestionRUDAPIView.as_view()          ,name="subTopic_edit"),
]
