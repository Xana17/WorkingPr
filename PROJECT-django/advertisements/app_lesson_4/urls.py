from django.urls import path 
from .views import lesson_4

urlpatterns = [
    path("http://127.0.0.1/lesson_4.", lesson_4)
]