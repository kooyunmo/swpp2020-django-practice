from django.db import models


# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(default=25)
    score = models.IntegerField(default=100)

    def introduce(self):
        print("Hello, my name is " + str(self.name) + "and my score is " + str(self.score) + "!")

    def __str__(self):
        return self.name
