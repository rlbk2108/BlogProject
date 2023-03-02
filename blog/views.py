from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly, DjangoModelPermissions, AllowAny

from blog.models import Car, Client, Sharing
from blog.serializers import ClientSerializer, CarSerializer, SharingSerializer


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [AllowAny]


class SharingViewSet(viewsets.ModelViewSet):
    queryset = Sharing.objects.all()
    serializer_class = SharingSerializer
    permission_classes = [AllowAny]


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [AllowAny]
