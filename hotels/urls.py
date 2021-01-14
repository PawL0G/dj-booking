from rest_framework.routers import DefaultRouter

from .views import HotelView, BookingViewSet

app_name = "hotels"

router = DefaultRouter()
router.register(r'hotels', HotelView, basename='hotels')
router.register(r'booking', BookingViewSet, basename='booking')
urlpatterns = router.urls
