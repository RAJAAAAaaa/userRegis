from rest_framework import serializers
from .models import *


class HistoryListingSerializer(serializers.ModelSerializer):

    class Meta:
        model = HistoricalRecords
        fields = '__all__'
