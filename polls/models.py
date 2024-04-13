import datetime

from django.db import models
from django.utils import timezone


class Election(models.Model):
    election_name = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    def __str__(self):
        return self.election_name


class Candidate(models.Model):
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    candidate_name = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.candidate_name