from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_page(request):
    return HttpResponse('''<html>
                        <head>
                        <title>To-Do lists</title>
                        <body>
                        <h1>To-Do lists</h1>
                        <input type="textbox" id="id_new_item" placeholder="Enter a to-do item" /> 
                        </body></html>''')