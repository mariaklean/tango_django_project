from django.shortcuts import render

from django.http import HttpResponse

def index(request):
    conext_dir={'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'rango/index.html',context=conext_dir)

def about(request):
    return HttpResponse("Rango says here is the about page. <a href='http://127.0.0.1:8000/'>Index</a>")
