from django.db import models


class Hero(models.Model):
  name = models.CharField(max_length=120)
  age = models.IntegerField(default=25)
  score = models.IntegerField(default=0)

  def __str__(self):
    return self.name

  def introduce(self):
    return 'Hello, my name is {} and my score is {}!'.format(self.name, self.score)

# Create your models here.
