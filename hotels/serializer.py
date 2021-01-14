from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

from .models import Booking, Hotel


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'description', 'pub_date', 'booking')

        validators = [
            UniqueTogetherValidator(
                queryset=Hotel.objects.all(),
                fields=['description']
            )
        ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        ordering = ('id',)
        fields = ('id', 'title', 'date_time', 'rating', 'origin')

        validators = [
            UniqueTogetherValidator(
                queryset=Booking.objects.all(),
                fields=['title']
            )
        ]