import datetime

from django.db import models
from django.utils import timezone

# Create your models here.
# n our simple poll app, we’ll create two models: Question and Choice.
# A Question has a question and a publication date. A Choice has two fields:
# the text of the choice and a vote tally. Each Choice is associated with a Question.


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        if self.pub_date > timezone.now():
            return False
        return self.pub_date + datetime.timedelta(days=1) >= timezone.now()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


