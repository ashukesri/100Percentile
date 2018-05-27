from django.conf.urls import url,include
from django.contrib import admin

from rest_framework.routers import DefaultRouter
from  users import views

router = DefaultRouter()
router.register('profile',views.UserProfileViewSet)
router.register('login',views.LoginViewSet, base_name='login')


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'',include(router.urls))
]
