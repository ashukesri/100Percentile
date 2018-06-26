# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from questions.models import *
from users.models import *
from django.db import models
from django.utils import timezone
from datetime import datetime
class BlogPost(models.Model):
    difficulty = (
        (1, ('Basic')),
        (2, ('Mediam')),
        (3, ('Hard'))
    )
    
    status_choice = (
        (1, ('Submited')),
        (2, ('Discarded')),
        (3, ('Reviewed')),
        (4, ('Publised'))
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="BlogPosts")
    difficultyLevel = models.IntegerField(choices=difficulty, default=1)
    status = models.IntegerField(choices=status_choice, default=1)
    title = models.CharField(max_length=200)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    
    def save(self, *args, **kwargs):
        if self.status == '4' and self.published_date== None:
            self.published_date= datetime.now()
            
        super(BlogPost, self).save(*args, **kwargs) 
        
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
    
class BlogPostDiscussion(models.Model):
    question = models.ForeignKey(BlogPost,on_delete=models.CASCADE,related_name='BlogPostDiscussions')
    user = models.ForeignKey(User, on_delete=models.CASCADE ,related_name="BlogPostDiscussionUser")
    comment = models.TextField(blank=False)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
