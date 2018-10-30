from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=1)
    score_2017 = models.IntegerField()
    score_2018 = models.IntegerField()
    users = models.ManyToManyField(User, blank=True)

    def __str__(self):
        return self.name



# class TeamScore(models.Model, Team):
#     game = models.ManyToManyField(Team)
#     date = models.DateTimeField()
#     score = models.IntegerField()

    # def __str__(self):
    #     return self.game