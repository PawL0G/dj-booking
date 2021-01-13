from rest_framework import viewsets
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from django.shortcuts import get_object_or_404
from rest_framework.response import Response

from .models import Booking, Hotel
from .serializer import BookingSerializer, HotelSerializer


# class ArticleView(APIView):
#
#     def get(self, request):
#         booking = Booking.objects.all()
#         serializer = BookingSerializer(booking, many=True)
#         return Response({"hotels": serializer.data})
#
#     def post(self, request, **pk):
#         saved_hotel = get_object_or_404(Booking.objects.all(), pk=pk)
#         booking = request.data.get('hotel')
#         serializer = BookingSerializer(data=booking)
#         if serializer.is_valid(raise_exception=True):
#             saved_hotel = serializer.save()
#         return Response({
#             "success": "Hotel '{}' created successfully".format(saved_hotel.title)
#         })
#
#     def put(self, request, **pk):
#         saved_hotel = get_object_or_404(Booking.objects.all(), pk=pk)
#         data = request.data.get('hotel')
#         serializer = BookingSerializer(instance=saved_hotel, data=data, partial=True)
#         if serializer.is_valid(raise_exception=True):
#             saved_hotel = serializer.save()
#         return Response({
#             "success": "Article '{}' updated successfully".format(saved_hotel.title)
#         })
#
#     def delete(self, request, **pk):
#         article = get_object_or_404(Booking.objects.all(), pk=pk)
#         article.delete()
#         return Response({
#             "message": "Article with id `{}` has been deleted.".format(pk)
#         }, status=204)


# class ArticleView(ListModelMixin, CreateModelMixin, GenericAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def perform_create(self, serializer):
#         author = get_object_or_404(Hotel, id=self.request.data.get('hotel_id'))
#         return serializer.save(author=author)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ArticleView(viewsets.ViewSet):
#     """
#     A simple ViewSet that for listing or retrieving users.
#     """
#     def list(self, request):
#         queryset = Booking.objects.all()
#         serializer = BookingSerializer(queryset, many=True)
#         return Response(serializer.data)
#     def retrieve(self, request, pk=None):
#         queryset = Booking.objects.all()
#         user = get_object_or_404(queryset, pk=pk)
#         serializer = BookingSerializer(user)
#         return Response(serializer.data)
#
#

class ArticleView(viewsets.ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()



# class ArticleView(ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
#
#     def perform_create(self, serializer):
#         author = get_object_or_404(Hotel, id=self.request.data.get('id'))
#         return serializer.save(author=author)
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


#
# class SingleArticleView(RetrieveUpdateDestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer
