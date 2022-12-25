from rest_framework import serializers

from .models import Employee, Position

class PositionSerializer(serializers.Serializer):
    position = serializers.CharField(max_length=20)
    department = serializers.CharField(max_length=20)

    def create(self, validated_data):
        return Position.objects.create(**validated_data)

class EmployeeSerializer(serializers.Serializer):
    fullname = serializers.CharField(max_length=30)
    birth_date = serializers.DateField()
    salary = serializers.FloatField()
    position = serializers.PrimaryKeyRelatedField(queryset=Position.objects.all(), many=False)

    def create(self, validated_data):
        return Employee.objects.create(**validated_data)