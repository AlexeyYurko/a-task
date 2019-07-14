# Create your views here.

import csv
from datetime import datetime

from django.db.models import Func, Sum
from django.http import HttpResponse
from django.shortcuts import render
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.filters import OrderingFilter

from .models import Record
from .serializers import RecordSerializerWithGroupBy, RecordSerializerWithoutGroupBy


def home(request):
    return render(request, 'index.html')


def import_csv(request):
    """
    Used to populate django model with data from csv file.
    Doesn't contain any check to "overpopulate" DB, so it need to be called only once
    """
    with open('./sample_data.csv') as f:
        data = csv.reader(f, delimiter=',')
        for row in data:
            if row[0] != 'date':
                record = Record.objects.create()
                record.date = datetime.strptime(row[0], '%d.%m.%Y')
                record.channel = row[1]
                record.country = row[2]
                record.os = row[3]
                record.impressions = int(row[4])
                record.clicks = int(row[5])
                record.installs = int(row[6])
                record.spend = float(row[7])
                record.revenue = float(row[8])
                record.cpi = record.spend / record.installs
                record.save()
    return HttpResponse('Sample data imported.<br>Please do not use this link again :)')


class RecordFilter(filters.FilterSet):
    os = filters.CharFilter(field_name='os')
    channel = filters.CharFilter(field_name='channel')
    country = filters.CharFilter(field_name='country')
    date_from = filters.DateFilter(field_name='date', lookup_expr='gte')
    date_to = filters.DateFilter(field_name='date', lookup_expr='lte')

    class Meta:
        model = Record
        fields = ['channel', 'os', 'country']


class RecordViewSet(generics.ListAPIView):
    filter_backends = (DjangoFilterBackend, OrderingFilter,)
    filterset_class = RecordFilter
    ordering_fields = '__all__'

    '''
    place where the DRY is DIE
    '''

    def get_queryset(self):
        class Round(Func):
            function = 'ROUND'
            arity = 2

        queryset = Record.objects.all()
        try:
            groupby = self.request.query_params['groupby']
        except (KeyError, TypeError):
            return queryset
        if not groupby:
            return queryset
        groupby_list = ''.join(groupby.lower().split('?')[0]).split(',')
        allowed_group_by = ['date', 'channel', 'country', 'os']
        filtered_group_by = [group for group in groupby_list if group in allowed_group_by]
        if not filtered_group_by:
            return queryset

        queryset = queryset.values(*filtered_group_by).annotate(clicks_sum=Sum('clicks'),
                                                                impressions_sum=Sum('impressions'),
                                                                installs_sum=Sum('installs'),
                                                                spend_sum=Round(Sum('spend'), 2),
                                                                revenue_sum=Round(Sum('revenue'), 2),
                                                                cpi_sum=Round(Sum('cpi'), 2)
                                                                )
        print(queryset.query)
        return queryset

    def get_serializer(self, *args, **kwargs):
        try:
            groupby = self.request.query_params['groupby']
        except (KeyError, TypeError):
            return RecordSerializerWithoutGroupBy(*args, **kwargs)
        if not groupby:
            return RecordSerializerWithoutGroupBy(*args, **kwargs)
        groupby_list = ''.join(groupby.lower().split('?')[0]).split(',')
        allowed_group_by = ['date', 'channel', 'country', 'os']
        filtered_group_by = [group for group in groupby_list if group in allowed_group_by]
        if not filtered_group_by:
            return RecordSerializerWithoutGroupBy(*args, **kwargs)
        return RecordSerializerWithGroupBy(*args, **kwargs)
