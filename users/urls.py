from django.conf.urls import url
                       
from .views import(     UserAnswerCreateAPIView,    
#                        UserAnswerRUDAPIView

                    )
                    
                    
urlpatterns = [
    
    url(r'submit-answer'    ,UserAnswerCreateAPIView.as_view()         ,name="submit_answer"),
#    url(r'edit-answer'    ,UserAnswerRUDAPIView.as_view()         ,name="edit_answer"),

]
