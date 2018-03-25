import datetime

from django.db import models
from django.utils import timezone

class Zipcode(models.Model):
    number = models.IntegerField(default=-1)
    vehicle_miles = models.IntegerField(default=0)
    
    def __str__(self):
        return "zip code: " + str(self.number)
    def lots_of_miles(self):
        return self.vehicle_miles > 10000

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now()
datetime.timedelta(days=1)

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
