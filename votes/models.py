from django.db import models
from django.utils import timezone

class Position(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=100)

    def __str__(self):
        return 'Position: {}'.format(self.name)

class Candidate(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    position= models.ForeignKey(Position, on_delete=models.CASCADE,
     null=True, blank=True)
    birthdate = models.DateTimeField()
    platform = models.TextField(max_length=100)

    def __str__(self):
        return 'Candidate: {}'.format(self.firstname)


class Vote(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE,
     null=True, blank=True)
    vote_datetime = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return 'Vote: {}'.format(self.candidate)
