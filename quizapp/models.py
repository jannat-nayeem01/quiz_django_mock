from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    user_type_choices = [
        ('admin','Admin'),
        ('participant','Participant')
    ]
    user_type = models.CharField(choices = user_type_choices)
    
    def __str__(self):
        return self.username
        
class Participant(models.Model):
    user = models.OneToOneField(CustomUser,on_delete=models.CASCADE,name='participant')
    name = models.CharField(max_length=200,null=True,blank=True)
    participant_class = models.IntegerField(null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender_choices = [
        ('F','Female'),
        ('M','Male')
    ]
    gender = models.CharField(choices=gender_choices,null = True,blank=True)
    institution = models.CharField(null=True,blank = True)
    
    def __str__(self):
        return self.user.username
class Quiz(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True,blank=True)
    def __str__(self):
        return self.title
class Question(models.Model):
    quiz = models.ForeignKey(Quiz,on_delete=models.CASCADE,related_name="questions")
    question = models.CharField(max_length=255)
    def __str__(self):
        return self.question
class Option(models.Model):
    question = models.ForeignKey(Question,on_delete=models.CASCADE,related_name='options')
    option = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)
    def __str__(self):
        return self.option
    
        
        
