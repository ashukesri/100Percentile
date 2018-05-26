from __future__ import unicode_literals
from django.contrib import admin

from questions.models import *


admin.site.register(Questions)
admin.site.register(QuestionImages)
admin.site.register(QuestionAnswers)
admin.site.register(Topics)
admin.site.register(SubTopics)
