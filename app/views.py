from django.shortcuts import render, redirect, HttpResponse

import random
import string
# Create your views here.
def home(request):
    return render(request, "home.html")

shorts = {}
def shorten(request):
    if request.method=="POST" :
        url = request.POST.get('url')
        short_url= ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        shorts[short_url] = url
    return render(request, "shorten.html", {"url":short_url})

def redirect_to_origin(request,short_url):
    if short_url in shorts :
        return redirect(shorts[short_url])
    else :
        return HttpResponse("invalid link")