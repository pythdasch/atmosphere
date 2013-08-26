# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from blog.models import Article, Category, last_articles, oneofeach
from newsletter.models import Newsletter
from blog.forms import ContactForm
from outils.mail_utils import contact_email


def coming_soon(request):
    news = get_object_or_404(Newsletter, name="main")
    return render(request, 'coming_soon.html', {
        'newsletter': news,
        })

def index(request):
    return render(request, 'index.html', {
        'oneofeach': oneofeach(),
        'last_articles': last_articles(20),
        'slider': last_articles(3),
        })

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            contact_email(contact)
            return render(request, 'contact_success.html')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {
        'form': form,
        })

def custom404(request):
    return render(request, '404.html')

def custom500(request):
    return render(request, '500.html')
