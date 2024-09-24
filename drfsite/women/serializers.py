from rest_framework import serializers

from drfsite.women.models import Women


class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ['title', 'content', 'time_create', 'time_update', 'is_published', 'cat']