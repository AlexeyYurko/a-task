from collections import OrderedDict

from rest_framework import serializers

from .models import Record


class RecordSerializer(serializers.HyperlinkedModelSerializer):
    """impressions_sum = serializers.IntegerField()
    installs_sum = serializers.IntegerField()
    clicks_sum = serializers.IntegerField()
    spend_sum = serializers.DecimalField(decimal_places=DECIMAL_PLACES, max_digits=MAX_DIGITS)
    revenue_sum = serializers.DecimalField(decimal_places=DECIMAL_PLACES, max_digits=MAX_DIGITS)
    cpi_sum = serializers.DecimalField(decimal_places=DECIMAL_PLACES, max_digits=MAX_DIGITS)
"""

    clicks_sum = serializers.IntegerField()

    class Meta:
        model = Record
        # fields = ('date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue', 'cpi',
        # 'impressions_sum', 'installs_sum', 'clicks_sum', 'spend_sum', 'revenue_sum', 'cpi_sum')
        fields = (
            'clicks_sum', 'date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue',
            'cpi')

    def to_representation(self, instance):
        """
        Mostly to hide date: null in grouped query.
        """
        ret = super().to_representation(instance)
        ret = OrderedDict(list(filter(lambda x: x[1], ret.items())))
        return ret
