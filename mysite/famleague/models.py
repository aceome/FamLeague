from django.db import models

from django.contrib.auth.models import User


class Team(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images/')
    category = models.CharField(max_length=1)
    score_2017 = models.IntegerField()
    score_2018 = models.IntegerField()
    users = models.ManyToManyField(User)

    def __str__(self):
        return self.name
