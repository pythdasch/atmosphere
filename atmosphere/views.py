# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category, last_articles, oneofeach
from newsletter.models import Newsletter
from blog.models import Contact
from outils.mail_utils import contact_email
from gallery.models import Gallery, first_photos
from general_config.models import MainSlider, Edito

def index(request):
    gallery = Gallery.objects.order_by('-created_at')[0]
    gallery_photos = first_photos(gallery, 12)
    slider = MainSlider.objects.all()[:10]
    edito = Edito.objects.order_by('-created_at')[0]
    return render(request, 'index.html', {
        'gallery': gallery,
        'gallery_photos': gallery_photos,
        'oneofeach': oneofeach(),
        'last_articles': last_articles(20),
        'edito': edito,
        'slider': slider,
        })

def contact(request):
    if request.method == 'POST':
        data = request.POST
        contact = Contact(name=data['name'], email=data["email"], subject=data["subject"], message=data["message"])
        contact = contact.save()
        contact_email(contact)
        return render(request, 'contact_success.html')
    return render(request, 'contact.html')

def custom404(request):
    return render(request, '404.html')

def custom500(request):
    return render(request, '500.html')
