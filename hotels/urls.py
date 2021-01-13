from rest_framework.routers import DefaultRouter

from .views import ArticleView

app_name = "hotels"

router = DefaultRouter()
router.register(r'hotels', ArticleView)
urlpatterns = router.urls
