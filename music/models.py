from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_name = models.CharField(max_length=250)
    genre = models.CharField(max_length=100)
    logo = models.CharField(max_length=1000)

    def __str__(self):
        return self.album_name


class Music(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)
    song_title = models.CharField(max_length=100)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
