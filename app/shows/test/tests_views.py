from django.test import TestCase, Client
from django.urls import reverse
from app.shows.views import *
import json

class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.index_url = reverse('shows:index')
        self.show_search_url = reverse('shows:show_search', args=['some'])
        self.first_air_date_year_url = reverse('shows:first_air_date_year', args=[1])
        self.popularity_url = reverse('shows:popularity', args=['1'])
        self.rating_url = reverse('shows:rating')

    def test_index_get_request(self):
        client = Client()
        response = client.get(self.index_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_show_search_get_request(self):
        client = Client()
        response = client.get(self.show_search_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_first_air_date_year_get_request(self):
        client = Client()
        response = client.get(self.first_air_date_year_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_popularity_get_request(self):
        client = Client()
        response = client.get(self.popularity_url)
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')


    def test_rating_post_request(self):
        client = Client()
        data = {'value': 0, 'tv_id':0}
        response = client.post(self.rating_url, json.dumps(data), content_type='application/json')
        self.assertEquals(response.status_code, 200)
