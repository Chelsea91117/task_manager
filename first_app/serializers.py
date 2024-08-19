from rest_framework import serializers
from django.utils import timezone
from .models import *


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['title', 'description', 'status', 'deadline']


class SubTaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubTask
        fields = '__all__'
        read_only_fields = ['created_at']


class CategoryCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

    def create(self, validated_data):
        name = validated_data.get('name')
        if Category.objects.filter(name=name).exists():
            raise serializers.ValidationError('Категория с таким названием уже существует.')
        return super().create(validated_data)

    def update(self, instance, validated_data):
        name = validated_data.get('name')
        if name != instance.name and Category.objects.filter(name=name).exists():
            raise serializers.ValidationError('Категория с таким названием уже существует.')
        return super().update(instance, validated_data)


class TaskDetailSerializer(serializers.ModelSerializer):
    subtask = SubTaskCreateSerializer()
    class Meta:
        model = Task
        fields = '__all__'
        read_only_fields = ['created_at']


class TaskCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        read_only_fields = ['created_at']

    def validate_deadline(self, value: str) -> int:
        value = timezone.make_aware(value.replace(tzinfo=None), timezone.get_current_timezone())
        if value < timezone.now():
            raise serializers.ValidationError("Дедлайн не может быть в прошлом")
        return value


