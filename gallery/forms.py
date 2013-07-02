# -*- coding:utf-8 -*-
from django import forms
from gallery.models import Image
import datetime


class MultiImageUploadForm(forms.ModelForm):
    """ This form is only used to handle the uploads """

    class Meta:
        fields = ('credit', 'display_caption', 'pub_date',)
        model = Image

    def __init__(self, *args, **kwargs):
        super(MultiImageUploadForm, self).__init__(*args, **kwargs)
        self.fields['pub_date'].initial = datetime.datetime.now()
