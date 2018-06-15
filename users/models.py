from django.db import models
from django.contrib.auth.models import User
from questions.models import *
from django.db.models.signals import post_save
from django.dispatch import receiver

class Profile(models.Model):
    roleAraay = (
        ('1',('Admin')),
        ('2',('Publisher')),
        ('3',('Reviewer')),
        ('4',('Visitor'))
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    role = models.CharField(max_length=100,choices=roleAraay,default='4')
    active = models.BooleanField(default=True)
    is_subscribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    follow= models.ManyToManyField(User,blank=False, related_name="profile_follow")

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

#    users = User.objects.all().select_related('profile')


class UserAnswer(models.Model):
    question = models.ForeignKey(Question,null=False)
    answer = models.ForeignKey(QuestionOption,null=False)
#    answer_sequence = models.PositiveIntegerField(null=True) #questions id
    user = models.ForeignKey(User)
    active = models.NullBooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __unicode__(self):
        return self.role
    
#class Follow(models.Model):
#    follower= models.ForeignKey(User, on_delete=models.CASCADE)
#    following= models.ForeignKey(User, on_delete=models.CASCADE)
#    
    
    
    
    
    
    
    
    
