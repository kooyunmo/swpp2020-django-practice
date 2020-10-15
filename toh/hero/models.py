from django.db import models

# Create your models here.
class Hero(models.Model):
  name = models.CharField(max_length=120)
  age = models.IntegerField(blank=True, null=True)
  score = models.IntegerField(blank=True, null=True, default=0)

  def introduce(self):
    print('Hello, my name is ' + str(self.name) + ' and my score is ' + str(self.score) + '!')

  def __str__(self):
    return self.name

  def __int__(self):
    return self.age