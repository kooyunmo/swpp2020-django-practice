from django.db import models

class Hero(models.Model):
  name = models.CharField(max_length=120)
  age = models.IntegerField(blank=True, null=True)
  score = models.IntegerField(default=0)

  def introduce(self):

    print("'Hello, my name is " + self.name + " and my score is " + str(self.score) + "!'")