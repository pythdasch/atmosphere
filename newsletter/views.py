# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from models import Newsletter, Subscriber
from forms import SubscriptionForm
from django.http import HttpResponse
from django.utils import simplejson
from outils.mail_utils import subscribe_mail
import re


def subscribe(request):
    news = get_object_or_404(Newsletter, name="main")
    if request.method == 'POST':
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            form = form.save()
            if request.LANGUAGE_CODE == 'en':
                subscribe_mail(request.POST['email'], news, language="en")
                return sub_success(request, news.id)
            else:
                subscribe_mail(request.POST['email'], news, language="fr")
                return sub_success(request, news.id)
        # data = request.POST
        # error = False
        # if not re.match(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$", data['email']):
        #     error = "incorrect"
        # already_sub = Subscriber.objects.filter(email=data['email'])
        # if already_sub:
        #     error = "already"
        # if not error:
        #     if request.LANGUAGE_CODE == 'en':
        #         form = Subscriber(email=data['email'], language="en")
        #         form.save()
        #         subscribe_mail(request.POST['email'], news, language="en")
        #         return HttpResponse(simplejson.dumps('inscri'))
        #     else:
        #         form = Subscriber(email=data['email'], language="fr")
        #         form.save()
        #         subscribe_mail(request.POST['email'], news, language="fr")
        #         return HttpResponse(simplejson.dumps('inscri'))
        # else:
        #     return HttpResponse(simplejson.dumps(error))
    else:
        form = SubscriptionForm()
    return render(request, 'newsletter/subscribe.html', {
        'newsletter': news,
        'form': form,
        })


def sub_success(request, object_id):
    news = get_object_or_404(Newsletter, pk=object_id)
    return render(request, 'newsletter/sub_success.html', {
        'newsletter': news,
        })


def newsletterview(request):
    news = Newsletter.objects.all()
    return render(request, 'newsletter/newsletters.html', {
        'news': news,
        })


def unsubscribe(request, object_id, subscriber_id):
    news = get_object_or_404(Newsletter, pk=object_id)
    sub = get_object_or_404(Subscriber, pk=subscriber_id)
    if request.method == 'POST':
        if request.POST['unsub'] == 'yes':
            sub.delete()
            return render(request, 'newsletter/unsub_success.html')
    return render(request, 'newsletter/unsubscribe.html', {
        'newsletter': news,
        'subscriber': sub,
        })
