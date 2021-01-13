from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import ArticleView

app_name = "hotels"

router = DefaultRouter()
router.register(r'hotels', ArticleView)
urlpatterns = router.urls

# urlpatterns = [
#     path('hotels/', ArticleView.as_view({'get': 'list'})),
#     path('hotels/<int:pk>', ArticleView.as_view({'get': 'retrieve'})),
#     # path('hotels/bookings/<int:pk>', SingleArticleView.as_view()),
# ]
