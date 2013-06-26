# -*- coding:utf-8 -*-
from pynliner import Pynliner
from django.core.mail import EmailMessage
from django.template import Context
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.core.urlresolvers import reverse
from newsletter.models import Subscriber
from atmosphere.settings import SITE_URL


class UnicodeSafePynliner(Pynliner):
    def _get_output(self):
        self.output = unicode(self.soup)
        return self.output


def subscribe_mail(email, newsletter):
    subscriber = get_object_or_404(Subscriber, email=email)
    template = get_template('mail/subscribe_mail.html')
    unsub_url = reverse('newsletter.views.unsubscribe', \
        kwargs={'object_id': newsletter.id, 'subscriber_id': subscriber.id})
    path = SITE_URL + unsub_url
    context = Context({'path': path, 'email': email})
    content = template.render(context)
    subject = u"[Newsletter] 13Atmosphere"
    msg = EmailMessage(subject, content, to=[email])
    msg.send()
