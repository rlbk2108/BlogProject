from rest_framework import serializers

from blog.models import Car, Client, Sharing


class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ['type', 'model', 'color', 'mileage']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['initials', 'balance']


class SharingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sharing
        fields = ['client', 'car', 'date_of_issue', 'date_of_return', 'cost_per_day', 'number_of_days', 'final_payment']
