# -*- coding:utf-8 -*-
from django.shortcuts import render, get_object_or_404
from models import Newsletter, Subscriber
from forms import SubscriptionForm
from django.http import HttpResponse, HttpRequest
from django.utils import simplejson
from outils.mail_utils import subscribe_mail


def subscribe(request, object_id):
    news = get_object_or_404(Newsletter, pk=object_id)
    if request.is_ajax():
        import ipdb;ipdb.set_trace()
        if request.method == 'POST':
            data = request.POST
            form = Subscriber(email=data['email'])
            form.save()
            # subscribe_mail(request.POST['email'], news)
            return HttpResponse(simplejson.dumps('inscri'))
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
    return render(request, 'newsletter/unsubscribe.html', {
        'newsletter': news,
        'subscriber': sub,
        })
