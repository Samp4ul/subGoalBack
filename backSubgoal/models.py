# myapp/models.py

from django.db import models

class Score(models.Model):
    score_actuel = models.IntegerField()

    def __str__(self):
        return f"Score: {self.score_actuel}"

class Subgoal(models.Model):
    score = models.IntegerField()
    nom = models.CharField(max_length=100)
    description = models.CharField(max_length=300,default="")

    def __str__(self):
        return f"{self.nom} ({self.score} pts)"
