"""
Serializers for request/response mapping
Frontend-compatible data structures
"""

from rest_framework import serializers


class JobListSerializer(serializers.Serializer):
    """Job list item"""
    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField(required=False)
    status = serializers.CharField(default='active')


class ImageUploadSerializer(serializers.Serializer):
    """Image upload request"""
    image = serializers.ImageField()
    job_id = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)


class AIProcessSerializer(serializers.Serializer):
    """AI processing request (image + text)"""
    image = serializers.ImageField(required=False)
    prompt = serializers.CharField()
    job_id = serializers.IntegerField(required=False)
    context = serializers.CharField(required=False)


class VoiceUploadSerializer(serializers.Serializer):
    """Voice upload request"""
    voice = serializers.FileField()
    job_id = serializers.IntegerField(required=False)
    description = serializers.CharField(required=False)


class AIResponseSerializer(serializers.Serializer):
    """AI response format"""
    status = serializers.CharField()
    result = serializers.CharField()
    confidence = serializers.FloatField(required=False)
    processing_time = serializers.FloatField(required=False)
