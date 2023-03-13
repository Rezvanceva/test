from rest_framework import serializers

from shop.models import Retail, Product, Provision, Contact


class RetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Retail
        fields = '__all__'


class RetailSerializer(serializers.ModelSerializer):
    product = serializers.SlugRelatedField(queryset=Product.objects.all(), slug_field='title')
    provision = serializers.SlugRelatedField(queryset=Provision.objects.all(), slug_field='title')
    contact = serializers.SlugRelatedField(queryset=Contact.objects.all(), slug_field='country')

    class Meta:
        model = Retail
        fields = '__all__'
        read_only_fields = ('receivables',)


class RetailUpdateSerializer(RetailSerializer):
    contact = serializers.PrimaryKeyRelatedField(queryset=Contact.objects.all())
