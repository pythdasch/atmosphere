from django.db import models

# Create your models here.

class Partenaire(models.Model):
    name = models.CharField(max_length=100)
    lien = models.URLField()
    logo = models.ImageField(upload_to="partenaires/")
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return "partenaire : " + self.name
