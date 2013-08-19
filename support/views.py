# -*- coding:utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib.auth.forms import AuthenticationForm


def index(request):
    if request.user.is_superuser:
        return render(request, 'support/index.html')
    else:
        return HttpResponseRedirect(reverse('support.views.login_in'))


def login_in(request):
    index_url = reverse('support.views.index')
    error_message = ''
    if request.user:
        if request.user.is_superuser:
            return HttpResponseRedirect(index_url)
        else:
            HttpResponseRedirect(reverse('atmosphere.views.index'))
    if request.method == 'POST':
        form = AuthenticationForm(request.POST)
        if form.is_valid:
            un = request.POST.get('username')
            pw = request.POST.get('password')
            from django.contrib.auth import authenticate, login
            # je l'enregistre et je l'authentifie
            user = authenticate(username=un, password=pw)
            if user:
                login(request, user)
                return HttpResponseRedirect(index_url)
            else:
                error_message = 'Email / password invalid'
        else:
            error_message = 'Aucun utilisateur à ce nom'
    else:
        form = AuthenticationForm()
    return render(request, 'support/login.html', {
        'form': form,
        'error': error_message,
        })
