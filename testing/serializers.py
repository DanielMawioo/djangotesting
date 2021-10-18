from rest_framework.serializers import ModelSerializer
from .models import Student

# serializers.py
class StudentSerializer(ModelSerializer):
     class Meta:
         model = Student
         fields = "__all__" 