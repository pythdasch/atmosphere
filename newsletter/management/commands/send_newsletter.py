from django.core.management.base import BaseCommand
from outils.mail_utils import UnicodeSafePynliner
from django.template.loader import render_to_string
from blog.models import Article
from newsletter.models import Subscriber, Newsletter
from django.core import mail
import datetime
from atmosphere.settings import SITE_URL


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        now = datetime.datetime.now()
        last_articles = Article.objects.order_by('-pub_date')[:5]
        len_articles = len(last_articles)
        news = Newsletter.objects.get(name='main')
        emails = []
        for sub in Subscriber.objects.all():
            subject = u'[13Atmosphere] Newsletter du  %s' % now
            message_html = UnicodeSafePynliner().from_string(render_to_string(
                    'newsletter/mail_newsletter.html', {
                    'last_articles': last_articles,
                    'len_articles': len_articles,
                    'SITE_URL': SITE_URL,
                    'news_id': news.id,
                    'subscriber': sub,
            }
            )).run()
            from_ = u'david-scheck@gmail.fr'
            # to_ = [teacher.email]
            to_ = [sub.email]
            email = mail.EmailMultiAlternatives(
                    subject, message_html, from_, to_)
            email.content_subtype = 'html'
            emails.append(email)
        connection = mail.get_connection()
        connection.open()
        connection.send_messages(emails)
        connection.close()
