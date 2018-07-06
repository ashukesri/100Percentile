
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings 
from django.conf.urls.static import static
from rest_framework.authtoken.views import ObtainAuthToken
#from rest_framework_jwt.views import obtain_jwt_token



urlpatterns = [ 
#    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^auth/', ObtainAuthToken.as_view()),
    url(r'^blog/', include('blogs.urls')),
    url(r'^user/', include('users.urls')),
    url(r'^question/', include('questions.urls')),
    url(r'^admin/'      , admin.site.urls),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL,document_root=settings.MEDIA_URL)
