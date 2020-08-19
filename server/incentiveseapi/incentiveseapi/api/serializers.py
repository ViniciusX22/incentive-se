from rest_framework import serializers
from .models import Incentive, Request


class IncentiveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Incentive
        fields = ['id', 'content', 'source']


class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = Request
        fields = ['id', 'content', 'source', 'status', 'created_at']
        read_only_fields = ['status']
