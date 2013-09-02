# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse



class Image(models.Model):
    """ Simple model for image file metadata """
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    thumbnail = models.ImageField(upload_to='images/thumbnail/', blank=True, null=True)

    def imagemAdmin(self):
        from sorl.thumbnail import get_thumbnail
        if self.img:
            try:
                im = get_thumbnail(self.img, '100x70', quality=80)
                return '<img src="{0}" />'.format(im.url)
            except:
                return ''
        return ''

    imagemAdmin.is_safe = True
    imagemAdmin.allow_tags = True
    imagemAdmin.short_description = u'Imagem'

    def imagem(self):
        from sorl.thumbnail import get_thumbnail
        if self.image:
            try:
                im = get_thumbnail(self.image, '80x45', quality=80)
                return im.url
            except:
                return ''

        return ''

    def __unicode__(self):
        return self.name

    def url(self):
        return reverse('imagem', args=(self.slug,))


class Gallery(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, max_length=50, help_text="Cet élèment n'est pas à modifier. Il permet de passer de page en page.")
    description = models.TextField()
    photos = models.ManyToManyField(Image)
    created_at = models.DateTimeField(auto_now_add=True)

    def all_galleries(self, length=20):
        return self.objects.order_by('created_at')[:length]

    def __unicode__(self):
        return 'Gallerie : ' + self.name
