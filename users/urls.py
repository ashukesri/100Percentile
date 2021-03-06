from django.conf.urls import url,include
from django.contrib.auth import views as auth_views     
from .views import(     UserAnswerCreateAPIView, 
                   ProfileRetrieveAPIView,
#                   ProfileListAPIView,
#                   UserListAPIView,
                   UserCreateAPIView,
#                        UserAnswerRUDAPIView

                    )
                    
                    
urlpatterns = [
    
#    url(r'^$'    ,UserListAPIView.as_view()         ,name="user_list"),
#    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'register'    ,UserCreateAPIView.as_view()         ,name="register"),
    url(r'profile/(?P<pk>\d+)'    ,ProfileRetrieveAPIView.as_view()         ,name="profile"),
    url(r'submit-answer'    ,UserAnswerCreateAPIView.as_view()         ,name="submit_answer"),
#    url(r'edit-answer'    ,UserAnswerRUDAPIView.as_view()         ,name="edit_answer"),

]

