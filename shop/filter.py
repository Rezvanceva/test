import django_filters.rest_framework

from shop.models import Retail


class RetailCountryFilter(django_filters.rest_framework.FilterSet):
    country = django_filters.CharFilter(field_name='contact__country')

    class Meta:
        model = Retail
        fields = ('country', )
