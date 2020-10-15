from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=25)
    score = models.IntegerField(default=0)

    def __str__(self):
        return self.name
    
    def introduce(self):
        return "Hello,my name is {n} and my score is {s}!".format(n = self.name, s = self.score)