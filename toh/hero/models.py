from django.db import models

# Create your models here.

class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(blank=True, null=True)

    def __str(self) :
        return self.name