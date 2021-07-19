from django.http import response
from django.test import SimpleTestCase
from django.urls import resolve, reverse
from app.shows.views import *

class TestUrls(SimpleTestCase):

    def test_index_url(self):
        url = reverse('shows:index')
        self.assertEquals(resolve(url).func, index)

    def test_show_search_url(self):
        url = reverse('shows:show_search', args=['some'])
        self.assertEquals(resolve(url).func, show_search)

    def test_first_air_date_year_url(self):
        url = reverse('shows:first_air_date_year', args=[1])
        self.assertEquals(resolve(url).func, first_air_date_year)

    def test_popularity_url(self):
        url = reverse('shows:popularity', args=['1'])
        self.assertEquals(resolve(url).func, popularity)

    def test_rating_url(self):
        url = reverse('shows:rating')
        self.assertEquals(resolve(url).func, rating)
