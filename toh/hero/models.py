from django.db import models
from django.db.models import CharField

class Hero(models.Model):
	name = CharField(max_length=120)

	def __str__(self):
		return self.name
