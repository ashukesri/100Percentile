from django.db import models
from django.contrib.auth.models import User
from questions.models import *


class UserProfile(models.Model):
    roleAraay = (
        (1,('Admin')),
        (2,('Visitor'))
    )
    user = models.OneToOneField(User, primary_key=True)
    role = models.CharField(max_length=100,choices=roleAraay,default=2)
    active = models.BooleanField(default=True)
    is_subscribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.role



class UserAnswer(models.Model):
    question = models.ForeignKey(Questions,null=False)
    answer = models.ForeignKey(QuestionAnswers,null=False)
    answer_sequence = models.PositiveIntegerField(null=True)
    user = models.ForeignKey(UserProfile)
    active = models.NullBooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.role
