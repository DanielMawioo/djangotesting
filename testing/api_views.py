from .models import Student
from rest_framework import generics
from .serializers import StudentSerializer


# api_view.py
class CreateStudentApiView(generics.CreateAPIView):
     queryset = Student.objects.all()
     serializer_class = StudentSerializer
        
