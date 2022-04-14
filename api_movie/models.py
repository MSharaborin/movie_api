from django.db import models


class Movie(models.Model):
    title = models.CharField("Title", max_length=256)
    description = models.TextField("Description")
    year = models.CharField("Year", max_length=256)
    type = models.CharField('Type', max_length=256)
    poster = models.ImageField("Poster", upload_to='img_movie', default='N/A')

    def __str__(self):
        return self.title