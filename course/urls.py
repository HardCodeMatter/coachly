from django.urls import path
from . import views


urlpatterns = [
    path('course/', views.course_list_view, name='course_list'),
    path('course/<int:id>/', views.course_detail_view, name='course_detail'),
    path('course/<int:id>/edit/', views.course_edit_view, name='course_edit'),
    path('course/create/', views.course_create_view, name='course_create'),
    path('course/join/', views.course_join_view, name='course_join'),
]
