from django.db import models
from gallery.models import Gallery
# Create your models here.

class Partenaire(models.Model):
    name = models.CharField(max_length=100)
    lien = models.URLField()
    logo = models.ImageField(upload_to="partenaires/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "partenaire : " + self.name


class MainSlider(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="slider/")
    article = models.ForeignKey(Gallery)

    def __unicode__(self):
        return "image : " + self.name


class Edito(models.Model):
    texte = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

class SocialNetwork(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField()

    def __unicode__(self):
        return self.name
