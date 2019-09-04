import datetime

from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):
    id = models.AutoField(primary_key=True, db_column='question_id')
    # id = models.IntegerField(primary_key=True, db_column='id')
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

    # class Meta:
    #     managed = False


class Choice(models.Model):
    id = models.AutoField(primary_key=True, db_column='choice_id')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    # question = models.ForeignKey(Question, on_delete=models.CASCADE, db_column='question_id')
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

    # class Meta:
    #     managed = False
    #     db_table = 'polls_choice'