from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views
from .views import *


router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename="category")
router.register(r'posts', views.PostViewSet, basename="post")

urlpatterns = [
    path('', include(router.urls)),
]
