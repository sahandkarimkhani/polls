from django.db import models

# Create your models here.

class Questions(models.Model):
    question_text = models.CharField(max_length=250)
    pub_date = models.DateTimeField('date of pub')

class Choice(models.Model):
    question = models.ForeignKey(Questions, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

