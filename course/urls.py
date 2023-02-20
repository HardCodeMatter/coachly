from django.urls import path
from . import views


urlpatterns = [
    path('course/', views.course_list_view, name='course_list'),
    path('course/create/', views.course_create_view, name='course_create'),
]
