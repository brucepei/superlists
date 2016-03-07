from django.test import TestCase
from django.http import HttpRequest
from django.core.urlresolvers import resolve

from study.views import home_page
# Create your tests here.

class HomePageTest(TestCase):
    def test_study_home_page(self):
        request = HttpRequest()
        
        handler = resolve('/study')
        
        self.assertEqual(handler.func, home_page)
    