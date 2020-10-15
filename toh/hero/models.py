from django.db import models

class Hero(models.Model):
  name = models.CharField(max_length=120)
  age = models.IntegerField(default=25, blank=True, null=True)
  score = models.IntegerField(default=0, blank=True, null=True)

  def introduce(self):
    print("'Hello, my name is %s and my score is %d!'" % (self.name, self.score))

  def __str__(self):
    return self.name

  def __repr__(self):
    return self.name


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

