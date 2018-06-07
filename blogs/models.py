# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from questions.models import *
from users.models import *
from django.db import models
from django.utils import timezone


class BlogPost(models.Model):
    difficulty = (
        ('1', ('Basic')),
        ('2', ('Mediam')),
        ('3', ('Hard'))
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="BlogPosts")
    difficultyLevel = models.CharField(max_length=100,choices=difficulty, default='1')
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __unicode__(self):
        return self.title



class BlogImage(models.Model):
    blog = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='BlogImages')
    image = models.ImageField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.image

    
class PersonTest(models.Model):
    first_name = models.CharField(max_length=33)
    last_name = models.CharField(max_length=33)
    
    def __str__(self):
        return first_name