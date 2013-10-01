from django.core.management.base import BaseCommand
from outils.mail_utils import UnicodeSafePynliner
from django.template.loader import render_to_string
from blog.models import Article
from newsletter.models import Subscriber, Newsletter
from general_config.models import Edito, SocialNetwork
from django.core import mail
import datetime
from atmosphere.settings import SITE_URL, SENDER_EMAIL
from atmosphere.settings_general import STATIC_URL
from outils.dateutils import french_month


class Command(BaseCommand):
    args = ''
    help = ''

    def handle(self, *args, **options):
        linked = SocialNetwork.objects.get(name='linkedin')
        viadeo = SocialNetwork.objects.get(name="viadeo")
        google = SocialNetwork.objects.get(name="google")
        now = datetime.datetime.now()
        last_articles = Article.objects.order_by('-pub_date')[:5]
        len_articles = len(last_articles)
        edito = Edito.objects.order_by('-created_at')[0]
        news = Newsletter.objects.get(name='main')
        emails = []
        for sub in Subscriber.objects.all():
            if sub.language == 'en':
                month = now.strftime('%B')
                subject = u'[13Atmosphere] Newsletter %s' % month
                message_html = UnicodeSafePynliner().from_string(render_to_string(
                        'newsletter/nl.html', {
                        'month': month,
                        'edito': edito,
                        'linked':linked,
                        'viadeo': viadeo,
                        'google': google,
                        'last_articles': last_articles,
                        'STATIC_URL': STATIC_URL,
                        'SITE_URL': SITE_URL,
                        'news_id': news.id,
                        'subscriber': sub,
                }
                )).run()
                from_ = SENDER_EMAIL
                to_ = [sub.email]

            else:
                month = french_month(now.month)
                subject = u'[13Atmosphere] Newsletter %s' % month
                message_html = UnicodeSafePynliner().from_string(render_to_string(
                        'newsletter/nl.html', {
                        'month':month,
                        'last_articles': last_articles,
                        'len_articles': len_articles,
                        'SITE_URL': SITE_URL,
                        'news_id': news.id,
                        'subscriber': sub,
                }
                )).run()
                from_ = SENDER_EMAIL
                to_ = [sub.email]
            email = mail.EmailMultiAlternatives(
                        subject, message_html, from_, to_)
            email.content_subtype = 'html'
            emails.append(email)
        connection = mail.get_connection()
        connection.open()
        connection.send_messages(emails)
        connection.close()
