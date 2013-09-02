# -*- coding:utf-8 -*-
from django.shortcuts import get_object_or_404, render
from gallery.models import Gallery

def single_gallery(request, gallery_slug):
    gallery = get_object_or_404(Gallery, slug=gallery_slug)
    return render(request, 'gallery/single.html',{
        'gallery': gallery,
        })
