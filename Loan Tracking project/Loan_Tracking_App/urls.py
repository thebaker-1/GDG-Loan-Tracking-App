from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LoanRecordViewSet

router = DefaultRouter()
router.register(r'loans', LoanRecordViewSet, basename='loan')

urlpatterns = [
    path('', include(router.urls)),
]