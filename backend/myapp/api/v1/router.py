from rest_framework import DefaultRouter
from viewsets import FichaViewSet

router = DefaultRouter()

router.register(r'fichas', FichaViewSet, basename="ficha")

urlparterns = router.urls