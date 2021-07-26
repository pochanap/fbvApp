from rest_framework import serializers
from .models import Student


class SudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ['id', 'name', 'score']
