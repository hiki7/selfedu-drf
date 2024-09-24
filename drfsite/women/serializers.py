from rest_framework import serializers

from .models import Women


class WomenSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)
    is_published = serializers.BooleanField(default=True)
    cat = serializers.IntegerField()

    def create(self, validated_data):
        return Women.objects.create(**validated_data)

# class WomenSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Women
#         fields = ['title', 'content', 'time_create', 'time_update', 'is_published', 'cat']