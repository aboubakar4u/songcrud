
from django.db import models

# Create your models here.

class  Artiste(models.Model):
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    first_name = models.CharField(max_length=400)
    last_name = models.CharField(max_length=400)
    age = models.IntegerField()

class Song(models.Model):
    title = models.CharField(max_length=100)
    date_released = models.DateTimeField(max_length=100)
    likes = models.CharField(max_length=100)
    artiste_id = models.CharField(max_length=100)

class Lyric(models.Model):
    song = models.ForeignKey('Song', on_delete=models.CASCADE)
    content = models.CharField(max_length=100)
    Song_id = models.CharField(max_length=100)