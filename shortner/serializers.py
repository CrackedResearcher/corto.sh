from rest_framework import serializers
from .models import Url, AnalyticData

class UrlCreateSerializer(serializers.ModelSerializer):

    url = serializers.URLField(source="original_url")

    class Meta:
        model = Url
        fields = ['url']

class UrlReadSerializer(serializers.ModelSerializer):

    url = serializers.URLField(source="original_url")
    short_code = serializers.CharField(source="slug")

    class Meta:
        model = Url
        fields = ['url', 'short_url', 'created_at', 'id', 'short_code']

class AnalyticsDataReadSerializer(serializers.ModelSerializer):

    url = serializers.URLField(source='url.original_url')
    short_url = serializers.URLField(source="url.short_url")
    last_visited = serializers.DateTimeField(source="updated_at")

    class Meta:
        model = AnalyticData
        fields = ['total_visits', 'url', 'short_url']