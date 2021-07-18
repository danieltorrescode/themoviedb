from django.shortcuts import render, redirect
from django.http import Http404, HttpResponse ,HttpResponseRedirect
from django.http import JsonResponse
from django.urls import reverse
import requests
import json


# Create your views here.

def authentication():
    api_key = '94065978e7ea33fdb51fb1520ae71aae'
    api_url = 'https://api.themoviedb.org/3/authentication/token/new?api_key=' + api_key
    response = requests.get(api_url)
    authentication = response.json()
    request_token = authentication["request_token"]

    api_url = 'https://api.themoviedb.org/3/authentication/token/validate_with_login?api_key=' + api_key
    payload = {
        'request_token': request_token,
        'username': 'jabexa4478',
        'password': 'SiHenkPmKtuy2iH',
    }
    response = requests.post(api_url, data=payload)
    authentication = response.json()
    request_token = authentication["request_token"]

    api_url = 'https://api.themoviedb.org/3/authentication/session/new?api_key=' + api_key
    payload = {'request_token': request_token}
    response = requests.post(api_url, data=payload)
    return response.json()

def index(request,page="1"):
    # api_key = '94065978e7ea33fdb51fb1520ae71aae'
    page = str(request.GET.get('page'))
    api_url = 'https://api.themoviedb.org/3/tv/popular?api_key=94065978e7ea33fdb51fb1520ae71aae&language=en-US&page=' + page
    response = requests.get(api_url)
    shows = response.json()
    return render(request, 'index.html', {'shows': shows })

def show_search(request,name="",page="1"):
    page = str(request.GET.get('page'))
    api_url = 'https://api.themoviedb.org/3/search/tv?api_key=94065978e7ea33fdb51fb1520ae71aae&language=en-US&page='+ page +'&include_adult=false&query=' + name
    response = requests.get(api_url)
    shows = response.json()
    return render(request, 'index.html', {'shows': shows })

def first_air_date_year(request,year="",page="1"):
    page = str(request.GET.get('page'))
    api_url = ' https://api.themoviedb.org/3/discover/tv?api_key=94065978e7ea33fdb51fb1520ae71aae&language=en-US&page='+ page +'&include_null_first_air_dates=false&first_air_date_year=' + str(year)
    response = requests.get(api_url)
    shows = response.json()

    return render(request, 'index.html', {'shows': shows })

def popularity(request,popularity="",page='1'):
    page = str(request.GET.get('page'))
    api_url = ' https://api.themoviedb.org/3/discover/tv?api_key=94065978e7ea33fdb51fb1520ae71aae&language=en-US&page='+ page +'&include_null_first_air_dates=false&sort_by=' + str(popularity)
    response = requests.get(api_url)
    shows = response.json()
    return render(request, 'index.html', {'shows': shows })

def rating_show(request):
    data = json.loads(request.body.decode("utf-8"))
    value = str(data['value'])
    tv_id = str(data['tv_id'])

    # print(value)
    # print(tv_id)
    session_id = authentication()
    print(session_id['session_id'])
    api_url = 'https://api.themoviedb.org/3/tv/'+ tv_id +'/rating?api_key=94065978e7ea33fdb51fb1520ae71aae&session_id=' + session_id['session_id']
    payload = {'value': value}
    response = requests.post(api_url, data=payload)
    print(response.json())
    return JsonResponse({"rating" : 'response.json()'})