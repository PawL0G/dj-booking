from django.db import models
from places.fields import PlacesField


class PatchedPlaceField(PlacesField):
    def value_to_string(self, obj):
        value = self.value_from_object(obj)
        return self.get_prep_value(value)


class Booking(models.Model):
    title = models.CharField(max_length=255)
    origin = PatchedPlaceField(max_length=25, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)
    rating = models.FloatField(default=0.0, help_text="Enter hotel rating", blank=True)
    is_published = models.BooleanField(default=True, verbose_name='Published')

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-date_time',)


class Hotel(models.Model):
    description = models.TextField(max_length=999)
    pub_date = models.DateTimeField('Choose your date to book', null=True)
    booking = models.ForeignKey('Booking', related_name='booking', verbose_name='hotel location', on_delete=models.CASCADE)

    @staticmethod
    def counter(count=0):
        count += 1

    class Meta:
        ordering = ('-pub_date',)

    def __str__(self):
        return self.__class__.__name__
