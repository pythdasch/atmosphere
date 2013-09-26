# -*- coding: utf-8 -*-
from django.db import models
from django.core.urlresolvers import reverse


class Author(models.Model):
    name = models.CharField(max_length=100)
    biography = models.TextField()
    image = models.ImageField(upload_to="gallery/author/")

    def __unicode__(self):
        return 'Auteur : ' + self.name


class Gallery(models.Model):
    name = models.CharField("thème", max_length=255)
    slug = models.SlugField(unique=True, max_length=50, help_text="Cet élèment n'est pas à modifier. Il permet de passer de page en page.")
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='gallery/', blank=True, null=True)
    author = models.ForeignKey(Author)
    meta_keywords = meta_keywords = models.CharField("Meta Keywords", max_length=255,
    help_text='Comma-delimited set of SEO keywords for meta tag', blank=True, null=True)
    meta_description = models.CharField("Meta Description", max_length=255,
    help_text='Content for description meta tag', blank=True, null=True)

    def all_galleries(self, length=20):
        return self.objects.order_by('created_at')[:length]

    def __unicode__(self):
        return 'Gallerie : ' + self.name

def first_photos(gallery, num_photo=1):
    gallery = Gallery.objects.get(pk=gallery.id)
    photos = gallery.photos.all()[:num_photo]
    return photos

def last_galleries(num_galleries=12):
    try:
        galleries = Gallery.objects.order_by('-created_at')[:num_galleries]
    except:
        raise Exception('Veuillez créer une gallerie au minimum')
    return galleries


class Image(models.Model):
    """ Simple model for image file metadata """
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to='images/')
    thumbnail = models.ImageField(upload_to='images/thumbnail/', blank=True, null=True, help_text="ne sert qu'à avoir le bon format à afficher")
    gallery = models.ForeignKey(Gallery, related_name="photos")
    pub_date = models.DateTimeField(auto_now_add=True)

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
