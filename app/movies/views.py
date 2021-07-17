from django.shortcuts import render
from django.http import Http404, HttpResponse
import requests

# Create your views here.

def django_view():
    # get the response from the URL
    response = requests.get('https://jsonplaceholder.typicode.com/posts/1')
    print( response.json() )
    return False

def index(request):
  django_view()
  return render(request, 'index.html', {'key': django_view()})

