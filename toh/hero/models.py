from django.db import models

# Create your models here.
class Hero(models.Model):
  name = models.CharField(max_length=120)
  age = models.IntegerField(blank=True, null=True)
  score = models.IntegerField(default=0)

  def __str__(self):
    return f'name={self.name}, age={self.age}' 

  def introduce(self):
    return('Hello, my name is '+ self.name + " and my score is " + str(self.score) + "!")