from rest_framework import serializers, viewsets
from .models import Booking, Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model: Hotel
        fields = ('description', 'pub_date', 'booking')


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        ordering = ('id',)
        fields = ('id', 'title', 'date_time', 'rating', 'origin')

    def validate(self, data):
        if data['title'] == data['title']:
            raise serializers.ValidationError("Duplicated title, please change with another")
        return data
