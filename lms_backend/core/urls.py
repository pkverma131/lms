from django.urls import path
from .views import home, CoursesListAPIView


urlpatterns = [
    path('', home, name='home'),
    path('api/courses/', CoursesListAPIView.as_view(), name='courses-list'),
]