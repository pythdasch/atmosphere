# -*- coding:utf-8 -*-
from django import forms
from models import Contact, Article
from tinymce.widgets import TinyMCE


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact


class ArticleForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE(attrs={'cols': 80, 'rows': 30}))

    class Meta:
        model = Article

    def save(self, *args, **kwargs):
        import ipdb;ipdb.set_trace()
        article = []
        return article
