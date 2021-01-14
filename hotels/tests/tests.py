from django.urls import reverse, resolve
from rest_framework import status
from rest_framework.test import APITestCase
from ..models import Booking


class TestEndpoints:

    def test_detail(self):
        path = reverse('hotels', kwargs={'pk': 1})
        assert resolve(path).view_name == 'hotels'


class TestCreation(APITestCase):

    def test_create(self):
        url = reverse('booking')
        data = {'name': 'Apps'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Booking.objects.count(), 1)
        self.assertEqual(Booking.objects.get().name, 'Apps')