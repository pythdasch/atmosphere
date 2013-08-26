# -*- coding:utf-8 -*-
from pynliner import Pynliner
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from newsletter.models import Subscriber
from atmosphere.settings import SITE_URL
from django.template.loader import render_to_string
from atmosphere.settings import SENDER_EMAIL, CONTACT_RECEIVER
from django.core import mail
from django.template import Context
from django.template.loader import get_template
from django.core.mail import EmailMessage


class UnicodeSafePynliner(Pynliner):
    def _get_output(self):
        self.output = unicode(self.soup)
        return self.output


def subscribe_mail(email, newsletter, language="fr"):
    emails = []
    subscriber = get_object_or_404(Subscriber, email=email)
    unsub_url = reverse('newsletter.views.unsubscribe', \
        kwargs={'object_id': newsletter.id, 'subscriber_id': subscriber.id})
    path = SITE_URL + unsub_url
    subject = u"[13Atmosphere] Inscription à la newsletter"
    if language =='en':
        message_html = UnicodeSafePynliner().from_string(render_to_string(
                'mail/subscribe_mail_en.html', {
                'unsub_url': path,
            }
        )).run()
    else:
        message_html = UnicodeSafePynliner().from_string(render_to_string(
                'mail/subscribe_mail.html', {
                'unsub_url': path,
            }
        )).run()
    from_ = SENDER_EMAIL
    # to_ = [teacher.email]
    to_ = [subscriber.email]
    email = mail.EmailMultiAlternatives(
            subject, message_html, from_, to_)
    email.content_subtype = 'html'
    emails.append(email)
    connection = mail.get_connection()
    connection.open()
    connection.send_messages(emails)
    connection.close()


def contact_email(contact):
    template = get_template('mail/contact_email.html')
    context = Context({'contact': contact})
    content = template.render(context)
    subject = u"[CONTACT] Une personne vous a contacté"
    email = EmailMessage(subject, content, to=[CONTACT_RECEIVER])
    email.send()
