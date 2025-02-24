import datetime

from django.db import models
from django.utils import timezone
from django.db.models import Sum

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")

    #Metodos
    def __str__(self):
        return self.question_text
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    #Metodos desafio
    #usage: Question.total_votes(Question)
    def total_votes(self): 
        return Choice.objects.aggregate(Sum('votes'))
    #usage: Question.has_votes(Question)
    def has_votes(self): 
        check_status = Question.objects.filter(choice__votes__isnull=False)
        if str(check_status) == "<QuerySet []>": #TO-DO: realizar essa comparacao sem o matching de string. I.E: If Query Null 
            return False
        else: 
            return True


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text
