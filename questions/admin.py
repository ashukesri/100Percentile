from __future__ import unicode_literals
from django.contrib import admin

from questions.models import *

admin.site.register(Question)
admin.site.register(QuestionImage)
admin.site.register(QuestionOption)
admin.site.register(Topic)
admin.site.register(SubTopic)
admin.site.register(QuestionSolution)
admin.site.register(QuestionDiscussion)
