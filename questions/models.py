from django.db import models


class Topic(models.Model):
    topic = models.CharField(max_length=100, null=False)
    active = models.NullBooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.topic
    
    def __str__(self):
        return self.topic


class SubTopic(models.Model):
    subTopic = models.CharField(max_length=100, null=False)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    active = models.NullBooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.subTopic
    
    def __str__(self):
        return self.subTopic


class Question(models.Model):
    questionType = (
        (1, ('subjective')),
        (2, ('objetive'))
    )
    difficulty = (
        (1, ('Basic')),
        (2, ('Mediam')),
        (3, ('Hard'))
    )
    question = models.CharField(max_length=2000, null=False)
    questionType = models.CharField(max_length=100,choices=questionType)
    topic = models.ForeignKey(Topic,on_delete=models.CASCADE,null=True)
    subTopic = models.ForeignKey(SubTopic,on_delete=models.CASCADE,null=True)
    difficultyLevel = models.CharField(max_length=100,choices=difficulty,default=1)
    totalAttempt = models.PositiveIntegerField(default=0)
    totalCorrectAttempt = models.PositiveIntegerField(default=0)
    is_subscribed = models.BooleanField(default=False)
    thrasoldTime = models.PositiveIntegerField(default=2)
    videoLink = models.URLField(null=True)
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.question



class QuestionImage(models.Model):
    
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.image



class QuestionAnswer(models.Model):

    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='QuestionAnswers')
    answer = models.CharField(max_length=1000,null=True)
    answer_sequence = models.PositiveIntegerField(null=False)
    is_right_option = models.BooleanField(default=False)
    image = models.ImageField(null=True)
    active = models.NullBooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     

    def __unicode__(self):
        return self.answer