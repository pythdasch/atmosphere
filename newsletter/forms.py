# -*- coding:utf-8 -*-
from django import forms
from models import Subscriber


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
