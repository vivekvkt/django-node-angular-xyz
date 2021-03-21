from django.shortcuts import render
from django.http import HttpResponseRedirect

import requests

from bs4 import BeautifulSoup

from .models import Link

def scrap(request):
    if request.method == "POST":
        site = request.POST.get('web','')
 
        page = requests.get(site)
        soup = BeautifulSoup(page.text,'html.parser')
        for link in soup.find_all('a'):
            link_address = link.get('href')
            link_text = link.string
            Link.objects.create(address_bar=link_address,name=link_text)
        return HttpResponseRedirect('/')
    else:
        data = Link.objects.all()
 
 
    return render(request,'web/result.html',{'data':data})
 
def clear(request):
    Link.objects.all().delete()
    return render(request,'web/result.html')