from django.db import models
from django.db.models import CharField, IntegerField

class Hero(models.Model):
	name = CharField(max_length=120)
	age = IntegerField(default=0)

	def __str__(self):
		return f'<Hero name="{self.name}", age={self.age}>'
