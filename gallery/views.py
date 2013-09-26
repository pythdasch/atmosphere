# -*- coding:utf-8 -*-
from django.shortcuts import get_object_or_404, render
from gallery.models import Gallery

def single_gallery(request, gallery_slug):
    gallery = get_object_or_404(Gallery, slug=gallery_slug)
    return render(request, 'gallery/single.html',{
        'gallery': gallery,
        })

def index_gallery(request):
    galleries = Gallery.objects.order_by('-created_at')[:10]
    for gallery in galleries:
        gallery.images_first = gallery.photos.order_by('-pub_date')[:5]
        gallery.images_snd = gallery.photos.order_by('-pub_date')[5:10]
    return render(request, 'gallery/index_gallery.html', {
        'galleries': galleries,
        })
