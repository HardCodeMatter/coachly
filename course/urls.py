from django.urls import path
from . import views


urlpatterns = [
    path('course/', views.course_list, name='course_list'),
    path('course/create/', views.course_create, name='course_create'),
]
