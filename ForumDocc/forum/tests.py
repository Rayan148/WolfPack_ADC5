from django.test import TestCase,SimpleTestCase,Client
from .models import Thread,Reply
from django.urls import resolve,reverse
from .views import *

class TestModel(TestCase):
    def test_Thread(self):
        obj=Thread.objects.create(title="aaa",description="hello")
        obj1=Thread.objects.get(title="aaa")
        self.assertEquals(obj1.title,'aaa')

class TestUrl(SimpleTestCase):
    def test_url(self):
        url=reverse("forum:thread",args=[1])
        self.assertEquals(resolve(url).func,thread)
