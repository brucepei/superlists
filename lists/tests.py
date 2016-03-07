from django.test import TestCase
from django.core.urlresolvers import resolve
from django.http import HttpRequest
from django.template.loader import render_to_string
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)
        
    def test_home_page_return_correct_html(self):
        request = HttpRequest()
        
        response = home_page(request)
        
        self.assertTrue(response.content.startswith(b'<html>'), "home_page starts with '<html'")
        self.assertIn(b'<title>To-Do lists</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'), "home_page ends with 'html/>'")
        #print "content: {}".format(repr(response.content.decode()))
        #print "template: {}".format(repr(render_to_string('lists/home.html')))
        self.assertEqual(
            response.content.decode(), render_to_string('lists/home.html', request=request),
            "home_page entirely matched with template"
        )
        
    def test_home_page_can_save_a_post_request(self):
        request = HttpRequest()
        request.method = 'POST'
        request.POST['item_text'] = "A new list item"
        
        response = home_page(request)
        
        self.assertIn("A new list item", response.content.decode())
        #print "response: {}".format(response.content.decode())
        #print "context: {}".format(repr(render_to_string('lists/home.html', request=request, context={
        #        'new_item_text': request.POST['item_text'],
        #    })))
        self.assertEqual(
            response.content.decode(), render_to_string('lists/home.html', request=request, context={
                'new_item_text': request.POST['item_text'],
            }),
            "post a request with to-do item return a page equals the home_page with variable replaced"
        )
    