from django.db import models


class Topics(models.Model):
    topic = models.CharField(max_length=100, null=False)
    active = models.NullBooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.topic


class SubTopics(models.Model):
    subTopic = models.CharField(max_length=100, null=False)
    topic = models.ForeignKey(Topics, on_delete=models.CASCADE)
    active = models.NullBooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.subTopic


class Questions(models.Model):
    questionType = (
        (1, ('subjective')),
        (2, ('objetive'))
    )
    difficulty = (
        (1, ('Basic')),
        (2, ('Mediam')),
        (3,('Hard'))
    )
    question = models.CharField(max_length=2000, null=False)
    type = models.CharField(max_length=100,choices=questionType)
    topic = models.ForeignKey(Topics,on_delete=models.CASCADE,null=True)
    subTopic = models.ForeignKey(SubTopics,on_delete=models.CASCADE,null=True)
    difficultyLevel = models.CharField(max_length=100,choices=difficulty,default=1)
    totalAttempt = models.PositiveIntegerField(null=True)
    totalCurrectAttempt = models.PositiveIntegerField(null=True)
    is_subscribed = models.BooleanField(default=False)
    thrasoldTime = models.TimeField(default='2 minute')
    videoLink = models.URLField(null=True)
    active = models.NullBooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     

    def __unicode__(self):
        return self.question



class QuestionImages(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    image = models.ImageField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.image



class QuestionAnswers(models.Model):
    questionType = (
        (1,('subjective')),
        (2,('objetive'))
    )
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer = models.CharField(max_length=1000,null=True)
    answer_sequence = models.PositiveIntegerField(null=False)
    answerType = models.PositiveIntegerField(choices=questionType,default=1)
    image = models.ImageField(null=True)
    active = models.NullBooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
     

    def __unicode__(self):
        return self.answer