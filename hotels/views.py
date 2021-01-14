from rest_framework import viewsets
from .models import Booking
from .serializer import BookingSerializer




class ArticleView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()



# class ArticleView(ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
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
#
#
#
# class SingleArticleView(RetrieveUpdateDestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer