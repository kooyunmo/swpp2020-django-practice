from django.db import models

class Hero(models.Model):
    name = models.CharField(max_length = 120)
    age = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name

    def introduce(self):
        return 'Hello, my name is ' + name + ' and my score is ' + str(self.score) + '!'