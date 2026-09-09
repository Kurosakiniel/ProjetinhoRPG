from rest_framework.routers import DefaultRouter
from myapp.api.v1.viewsets import FichaViewSet

router = DefaultRouter()

router.register(r'fichas', FichaViewSet, basename="ficha")

urlpatterns = router.urls