from collections import OrderedDict

from rest_framework import serializers

from .models import Record


class RecordSerializerWithGroupBy(serializers.HyperlinkedModelSerializer):
    impressions_sum = serializers.IntegerField()
    installs_sum = serializers.IntegerField()
    spend_sum = serializers.FloatField()
    revenue_sum = serializers.FloatField()
    cpi_sum = serializers.FloatField()
    clicks_sum = serializers.IntegerField()

    class Meta:
        model = Record
        fields = ('date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue', 'cpi',
                  'impressions_sum', 'installs_sum', 'clicks_sum', 'spend_sum', 'revenue_sum', 'cpi_sum')

    def to_representation(self, instance):
        """
        Mostly to hide date: null in grouped query.
        """
        ret = super().to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret


class RecordSerializerWithoutGroupBy(RecordSerializerWithGroupBy):
    class Meta:
        model = Record
        fields = ('date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue',
                  'cpi')
