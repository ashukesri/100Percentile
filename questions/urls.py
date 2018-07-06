from django.conf.urls import url
                       
from .views import(     
    AddQuestionCreateAPIView,
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
                   
    QuestionSolutionCreateAPIView,
    QuestionSolutionRUDAPIView,
    
    QuestionDiscussionCreateAPIView,
    QuestionDiscussionRUDAPIView,
)
                    
                    
urlpatterns = [
    
    url(r'^$'                             ,QuestionListAPIView.as_view()            ,name="questions"),
    url(r'user'                           ,UserQuestionListAPIView.as_view()        ,name="user_questions"),
    url(r'create'                ,AddQuestionCreateAPIView.as_view()       ,name="question_create"),
    url(r'edit/(?P<pk>\d+)'      ,QuestionRUDAPIView.as_view()             ,name="question_edit"),
    url(r'edit-image/(?P<pk>\d+)',QuestionImageRUDAPIView.as_view()        ,name="question_edit_image"),  
    
    url(r'option-create'                  ,QuestionOptionCreateAPIView.as_view()    ,name="question_answer_create"),
    url(r'option-edit/(?P<pk>\d+)'        ,QuestionOptionRUDAPIView.as_view()       ,name="question_answer_edit"),
    ###################
    url(r'solution-create'                ,QuestionSolutionCreateAPIView.as_view()  ,name="question_solution_create"),
    url(r'solution-edit/(?P<pk>\d+)'      ,QuestionSolutionRUDAPIView.as_view()     ,name="question_solution_edit"),
    
    url(r'discussion-create'              ,QuestionDiscussionCreateAPIView.as_view(),name="discussion_create"),
    url(r'discussion-edit/(?P<pk>\d+)'    ,QuestionDiscussionRUDAPIView.as_view()   ,name="discussion_edit"),
    ###################
    
    url(r'topic-create'                   ,TopicCreateAPIView.as_view()       ,name="topic_create"),
    url(r'topic-edit/(?P<pk>\d+)'         ,TopicRUDAPIView.as_view()             ,name="topic_edit"),
     
    url(r'subTopic-create'                ,SubTopicCreateAPIView.as_view()       ,name="subTopic_create"),
    url(r'subTopic-edit/(?P<pk>\d+)'      ,SubTopicRUDAPIView.as_view()             ,name="subTopic_edit"),
]
