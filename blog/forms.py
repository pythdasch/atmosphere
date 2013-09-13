# -*- coding:utf-8 -*-
from django import forms
from models import Contact, Article

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
