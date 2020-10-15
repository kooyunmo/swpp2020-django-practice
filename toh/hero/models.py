from django.db import models
from django.db.models import CharField, IntegerField, ManyToManyField, ForeignKey

class Hero(models.Model):
	name = CharField(max_length=120)
	age = IntegerField(default=0)

	def __str__(self):
		return f'<Hero name="{self.name}", age={self.age}>'

class Team(models.Model):
	name = CharField(max_length=120)
	leader = ForeignKey(
		Hero,
		on_delete=models.CASCADE,
		related_name="leader_set"
	)
	members = ManyToManyField(
		Hero,
		related_name="teams"
	)
	def __str__(self):
		return f'<Team name="{self.name}">'
