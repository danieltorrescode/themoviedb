from django.shortcuts import render
from django.http import Http404, HttpResponse
import requests

# Create your views here.

def get_shows():
    # get the response from the URL
    api_key = '94065978e7ea33fdb51fb1520ae71aae'
    api_url = 'https://api.themoviedb.org/3/tv/popular?api_key=94065978e7ea33fdb51fb1520ae71aae&language=en-US&page=1'
    response = requests.get(api_url)
    shows = response.json()


    # api_url = 'https://api.themoviedb.org/3/authentication/token/new?api_key=' + api_key
    # response = requests.get(api_url)
    # authentication = response.json()
    # request_token = authentication["request_token"]
    # print(request_token)

    # api_url = 'https://www.themoviedb.org/authenticate/allow/' + request_token
    # response = requests.get(api_url)
    # print(response.headers)

    # api_url = 'https://api.themoviedb.org/3/authentication/session/new?api_key=' + api_key
    # payload = {'request_token': request_token}
    # response = requests.post(api_url, data=payload)
    # print(response.json())
    return response.json()

def index(request):
    shows = get_shows()
    return render(request, 'index.html', {'shows': shows })

