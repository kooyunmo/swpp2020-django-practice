from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=25)
    score = models.IntegerField(default=100)

    def introduce(self):
        print('Hello, my name is {} and my score is {}!'.format(self.name, self.score))

    def __str__(self):
        return self.name

class Team(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE, # when the leader is deleted, team will be deleted
        related_name='leader_set', # hero.leader_set returns QuerySet of teams which leader is hero
    )
    members = models.ManyToManyField(
        Hero,
        related_name='teams',
    )

    def __str__(self):
        return self.name