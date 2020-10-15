from django.db import models
from jsonfield import JSONField

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def introduce(self):
        name = self.name
        score = self.score
        return 'Hello, my name is {} and my score is {}!'.format(name, score)


class Team(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
        related_name='leader_set',
    )
    members = models.ManyToManyField(
        Hero, 
        related_name='teams',
    )

    def __str__(self):
        return self.name

