from django.contrib import admin
from users.models import *

admin.site.register(UserProfile)
admin.site.register(UserAnswer)