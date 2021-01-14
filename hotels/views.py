from rest_framework import viewsets

from .models import Booking, Hotel
from .serializer import BookingSerializer, HotelSerializer


class BookingViewSet(viewsets.ReadOnlyModelViewSet):
    serializer_class = HotelSerializer
    queryset = Hotel.objects.all()

    def perform_create(self, serializer):
        serializer.save(serializer_class=self.request.title)


class HotelView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()

    def perform_create(self, serializer):
        serializer.save(serializer_class=self.request.title)


# class SingleHotelView(ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#
#
#     def perform_create(self, serializer):
#         queryset = get_object_or_404(Hotel, id=self.request.data.get('id'))
#         return serializer.save(queryset=queryset)
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
