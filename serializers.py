from rest_framework import serializers

from .models import CompanyModel, ContactModel, OrderModel

class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyModel
        fields = ('__all__')

class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactModel
        fields = ('__all__') 

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderModel
        fields = ('__all__')       