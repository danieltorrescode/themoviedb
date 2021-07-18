from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse ,HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
import requests

# Create your views here.

def get_shows():
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

def index(request,name=""):
    # api_key = '94065978e7ea33fdb51fb1520ae71aae'
    api_url = 'https://api.themoviedb.org/3/tv/popular?api_key=94065978e7ea33fdb51fb1520ae71aae&language=en-US&page=1'
    response = requests.get(api_url)
    shows = response.json()
    return render(request, 'index.html', {'shows': shows })

def show_search(request,name=""):
    api_url = 'https://api.themoviedb.org/3/search/tv?api_key=94065978e7ea33fdb51fb1520ae71aae&language=en-US&page=1&include_adult=false&query=' + name
    response = requests.get(api_url)
    shows = response.json()
    return render(request, 'index.html', {'shows': shows })

def first_air_date_year(request,year=""):
    api_url = ' https://api.themoviedb.org/3/discover/tv?api_key=94065978e7ea33fdb51fb1520ae71aae&language=en-US&page=1&include_null_first_air_dates=false&first_air_date_year=' + str(year)
    response = requests.get(api_url)
    shows = response.json()
    return render(request, 'index.html', {'shows': shows })

def first_air_date_year(request,year=""):
    api_url = ' https://api.themoviedb.org/3/discover/tv?api_key=94065978e7ea33fdb51fb1520ae71aae&language=en-US&page=1&include_null_first_air_dates=false&first_air_date_year=' + str(year)
    response = requests.get(api_url)
    shows = response.json()
    return render(request, 'index.html', {'shows': shows })