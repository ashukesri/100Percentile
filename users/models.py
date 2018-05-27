from django.db import models
from django.contrib.auth.models import User
from questions.models import *
from django.contrib.auth.models import User,BaseUserManager
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser

class UserProfileManager(BaseUserManager):
    def create_user(self,email,password=None):
        
        if not email:
            raise ValueError("Users must have an email address")
            
        email=self.normalize_email(email)
        user=self.model(email=email)
        
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self,email,password):
        
        user=self.create_user(email,password)
        
        user.is_superuser = True
        user.role=1
        user.save(using=self._db)
        return user
        
    
class UserProfile(AbstractBaseUser, PermissionsMixin):
    roleAraay = (
        (1,('Admin')),
        (2,('Visitor'))
    )
    email= models.EmailField(max_length=100,unique=True)
    role = models.CharField(max_length=100,choices=roleAraay,default=2)
    active = models.BooleanField(default=True)
    is_subscribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserProfileManager()
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []
    
    def __str__(self):
        return self.email

    def __unicode__(self):
        return self.role


#class UserProfile(models.Model):
#    roleAraay = (
#        (1,('Admin')),
#        (2,('Visitor'))
#    )
#    user = models.OneToOneField(User, primary_key=True)
#    role = models.CharField(max_length=100,choices=roleAraay,default=2)
#    active = models.BooleanField(default=True)
#    is_subscribed = models.BooleanField(default=False)
#    created_at = models.DateTimeField(auto_now_add=True)
#    updated_at = models.DateTimeField(auto_now=True)
#
#
#    def __unicode__(self):
#        return self.role



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
