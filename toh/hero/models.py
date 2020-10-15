from django.db import models

# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=120)
    age = models.IntegerField(blank=True, null=True)
    score = models.IntegerField(default=0)

    def __str__(self):
        return 'I am ' + self.name

    def introduce(self):
        return 'Me {}, me score {}'.format(self.name, self.score)

class Team(models.Model):
    name = models.CharField(max_length=120)
    leader = models.ForeignKey(
        Hero,
        on_delete=models.CASCADE,
        related_name='leader_set'
    )
    members = models.ManyToManyField(
        Hero,
        related_name='teams'
    )

    def __str__(self):
        return 'Team ' + self.name
