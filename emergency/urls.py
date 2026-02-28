from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmergencyContactViewSet, SOSAlertViewSet

router = DefaultRouter()
router.register(r'contacts', EmergencyContactViewSet, basename='contact')
router.register(r'sos', SOSAlertViewSet, basename='sos')

urlpatterns = [
    path('', include(router.urls)),
]
