from rest_framework.routers import DefaultRouter
from rest_example.applications.views import ApplicationViewSet


router = DefaultRouter()

router.register(r'', ApplicationViewSet)

urlpatterns = router.urls

