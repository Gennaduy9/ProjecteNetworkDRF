from rest_framework import serializers
from netstore.models import Seller

class SellerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        fields = ['id', 'seller_type', 'title', 'level', 'debt', 'created', 'contact', 'supplier', 'product']


class SellerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seller
        exclude = ('debt',)