import django_filters
from .models import Position


class PostFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    type = django_filters.CharFilter(field_name='type', lookup_expr='icontains')
    gramm = django_filters.CharFilter(field_name='gramm', lookup_expr='icontains')
    sostav = django_filters.CharFilter(field_name='sostav', lookup_expr='icontains')
    price = django_filters.CharFilter(field_name='price', lookup_expr='icontains')

    class Meta:
        model = Position
        fields = ['name', 'type']