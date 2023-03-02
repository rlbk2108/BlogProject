from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'cars', views.CarViewSet, basename="car")
router.register(r'clients', views.ClientViewSet, basename="client")
router.register(r'sharings', views.SharingViewSet, basename="share")

urlpatterns = [
    path('', include(router.urls)),
]
