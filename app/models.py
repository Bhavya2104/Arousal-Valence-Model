from django.db import models

# Create your models here.

class GameSession(models.Model):
    gameid = models.IntegerField(blank=False)
    valence = models.FloatField(blank=False)
    arousal = models.FloatField(blank=False)
    intensity = models.FloatField(blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # def __str__(self):
    #     return self.emotion