from rest_framework import serializers
from .models import Student2

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=100)
    class Meta:
        model=Student2
        fields='__all__'

from rest_framework import serializers
from .models import Student

class StudentSerializer1(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['phone', 'password']  # Include other profile fields as needed
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.phone = validated_data.get('phone', instance.phone)
        instance.password = validated_data.get('password', instance.password)
        # Update other profile fields as needed
        instance.save()
        return instance
