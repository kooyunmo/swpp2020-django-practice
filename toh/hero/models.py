from django.db import models

# Create your models here.
class Hero(models.Model):
	name = models.CharField(max_length=120)
	age = models.IntegerField(default=25)
	score = models.IntegerField(default=0)

	def __str__(self):
		return self.name
	def score_default():
		return {"score": 0}
	def introduce(self):
		print(f'Hello, my name is {self.name} and my score is {self.score}!')

