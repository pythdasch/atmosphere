
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from django.test import TestCase
from django.test.client import Client
from newsletter.models import Newsletter, Subscriber
from django.test.client import RequestFactory
from atmosphere.views import index
from newsletter.views import subscribe, sub_success, unsubscribe

class NewsletterTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.newsletter = Newsletter.objects.create(name="main")
        self.subscriber = Subscriber.objects.create(email='test@test.fr')
        self.subscriber.save()
        self.newsletter.save()

    def test_newsletter_pages(self):
        request = self.factory.get('/test/')
        request1 = self.factory.get('/newsletter/subscribe/1')
        req_success = self.factory.get('/newsletter/sub_success/1')

        response = index(request)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        response = subscribe(request1, object_id="1")
        self.assertEquals(response.status_code, 200)

        response = sub_success(req_success, object_id="1")
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/sub_success.html')

    def test_sub_unsub(self):
        request = self.factory.get('/newsletter/unsubscribe/1/1')

        response = unsubscribe(request, object_id=self.newsletter.id, subscriber_id=self.subscriber.id)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'newsletter/unsubscribe.html')


