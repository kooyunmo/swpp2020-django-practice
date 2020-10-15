from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(default=22)
    score = models.IntegerField(default=0)
    def __str__(self):
        return self.name

    def introduce(self):
        return ('Hello, my name is ' + self.name + 'and my score is '+ str(self.score)+'!')

class Team(models.Model):
    name = models.CharField(max_length=200)
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