# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from questions.models import *
from users.models import *
from django.db import models
from django.utils import timezone


class BlogPosts(models.Model):
    difficulty = (
        (1, ('Basic')),
        (2, ('Mediam')),
        (3, ('Hard'))
    )
    author = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    difficultyLevel = models.CharField(max_length=100,choices=difficulty, default=1)
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title



class BlogImages(models.Model):
    blog = models.ForeignKey(BlogPosts,on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.image