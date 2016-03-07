from django.shortcuts import render

# Create your views here.
def home_page(request):
    print "study home_page!"
    return render(request, 'study/home.html')