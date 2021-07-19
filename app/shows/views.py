from django.conf import settings
from django.http import Http404, HttpResponse ,HttpResponseRedirect
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
import  json, requests

# authentication function make multples calls to the external API
# require api_key generated at te admin panel of the provider API
#  this api_key and the base url can be change at the settin.py of the project

def authentication():
    #  get the first request_token with the api_key
    api_url = f'{ settings.BASE_URL }/authentication/token/new?api_key={ settings.API_KEY }'
    response = requests.get(api_url)
    authentication = response.json()
    request_token = authentication["request_token"]

    # get the second request_token with the api_key and the first token
    # also the credentials of the user are need it
    # to get the session_id
    api_url = f'{ settings.BASE_URL }/authentication/token/validate_with_login?api_key={ settings.API_KEY }'
    payload = {
        'request_token': request_token,
        'username': settings.API_USERNAME,
        'password': settings.API_PASSWORD,
    }
    response = requests.post(api_url, data=payload)
    authentication = response.json()
    request_token = authentication["request_token"]

    # finally get the session_id which allow to rate the shows later in the code
    api_url = f'{ settings.BASE_URL }/authentication/session/new?api_key={ settings.API_KEY }'
    payload = {'request_token': request_token}
    response = requests.post(api_url, data=payload)
    session_id = response.json()
    return session_id['session_id']

# get list of most popular tv shows
def index(request,page="1"):
    page = str(request.GET.get('page'))
    api_url = f'{ settings.BASE_URL }/tv/popular?api_key={ settings.API_KEY }&page={ page }'
    response = requests.get(api_url)
    shows = response.json()
    return render(request, 'index.html', {'shows': shows })

# filter list of tv shows by name
def show_search(request,name="",page="1"):
    page = str(request.GET.get('page'))
    api_url = f'{ settings.BASE_URL }/search/tv?api_key={ settings.API_KEY }&page={ page }'
    api_url += f'&include_adult=false&query={ name }'
    response = requests.get(api_url)
    shows = response.json()
    return render(request, 'index.html', {'shows': shows })

# filter list of tv shows by releases date
def first_air_date_year(request,year="",page="1"):
    page = str(request.GET.get('page'))
    api_url = f'{ settings.BASE_URL }/discover/tv?api_key={ settings.API_KEY }&page={ page }'
    api_url += f'&include_null_first_air_dates=false&first_air_date_year={ str(year) }'
    response = requests.get(api_url)
    shows = response.json()
    return render(request, 'index.html', {'shows': shows })

# sort tv shows by popularity
def popularity(request,popularity="",page='1'):
    page = str(request.GET.get('page'))
    api_url = f'{ settings.BASE_URL }/discover/tv?api_key={ settings.API_KEY }&page={ page }'
    api_url += f'&include_null_first_air_dates=false&sort_by={ popularity }'
    response = requests.get(api_url)
    shows = response.json()
    return render(request, 'index.html', {'shows': shows })

# allows to vote for the choosen tv show
def rating_show(request):
    data = json.loads(request.body.decode("utf-8"))
    value = str(data['value'])
    tv_id = str(data['tv_id'])
    session_id = authentication()
    api_url = f'{ settings.BASE_URL }/tv/{ tv_id }/api_key={ settings.API_KEY }&session_id={ session_id }'
    payload = {'value': value}
    response = requests.post(api_url, data=payload)
    return JsonResponse({"rating" : 'response.json()'})