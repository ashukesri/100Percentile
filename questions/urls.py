from django.conf.urls import url
                       
from .views import(     AddQuestionCreateAPIView,
                        QuestionListAPIView,
                        QuestionRUDAPIView,
                        QuestionImageRUDAPIView,
                   
                        TopicCreateAPIView,
                        TopicRUDAPIView,
                        SubTopicCreateAPIView,
                        SubTopicRUDAPIView,
                   
                        QuestionAnswerCreateAPIView,
                        QuestionAnswerRUDAPIView,
                        )
                    
                    
urlpatterns = [
    
    url(r'^$'                              ,QuestionListAPIView.as_view()         ,name="questions"),
    url(r'question-create'                 ,AddQuestionCreateAPIView.as_view()    ,name="question_create"),
    url(r'question-edit/(?P<pk>\d+)/'      ,QuestionRUDAPIView.as_view()          ,name="question_edit"),
    url(r'question-edit-image/(?P<pk>\d+)/',QuestionImageRUDAPIView.as_view()     ,name="question_edit_image"),  
    
    url(r'answer-create'                   ,QuestionAnswerCreateAPIView.as_view() ,name="question_answer_create"),
    url(r'answer-edit/(?P<pk>\d+)/'        ,QuestionAnswerRUDAPIView.as_view()    ,name="question_answer_edit"),
    
    
    url(r'topic-create'                    ,AddQuestionCreateAPIView.as_view()    ,name="topic_create"),
    url(r'topic-edit/(?P<pk>\d+)/'         ,QuestionRUDAPIView.as_view()          ,name="topic_edit"),
     
    url(r'subTopic-create'                 ,AddQuestionCreateAPIView.as_view()    ,name="subTopic_create"),
    url(r'subTopic-edit/(?P<pk>\d+)/'      ,QuestionRUDAPIView.as_view()          ,name="subTopic_edit"),
]
