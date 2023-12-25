from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .models import Courses
from .serializers import CoursesSerializer


def home(request):
    return HttpResponse("Welcome to the Core App!")

class CoursesListAPIView(generics.ListAPIView):
    queryset = Courses.objects.all()
    serializer_class = CoursesSerializer
