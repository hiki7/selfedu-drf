from rest_framework import serializers

from drfsite.women.models import Women


class WomenSerialzier(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(auto_now_add=True)
    time_update = serializers.DateTimeField(auto_now=True)
    is_published = serializers.BooleanField(default=True)
    cat = serializers.IntegerField()

# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ['title', 'content', 'time_create', 'time_update', 'is_published', 'cat']