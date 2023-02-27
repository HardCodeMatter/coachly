from django.urls import path
from . import views


urlpatterns = [
    path('course/', views.course_list_view, name='course_list'),
    path('course/<int:id>/', views.course_detail_view, name='course_detail'),
    path('course/<int:id>/edit/', views.course_edit_view, name='course_edit'),
    path('course/create/', views.course_create_view, name='course_create'),
    path('course/join/', views.course_join_view, name='course_join'),

    path('course/announcement/<int:id>/delete/', views.announcement_delete_view, name='announcement_delete'),

    path('course/<int:id>/task/', views.task_list_view, name='task_list'),
    path('course/<int:course_id>/task/<int:task_id>/', views.task_detail_view, name='task_detail'),
    path('course/<int:course_id>/task/<int:task_id>/edit/', views.task_edit_view, name='task_edit'),
    path('course/<int:id>/task/create/', views.task_create_view, name='task_create'),

    path('course/<int:id>/grade/', views.grade_list_view, name='grade_list'),
    path('course/<int:course_id>/grade/<int:grade_id>/edit/', views.grade_edit_view, name='grade_edit'),

    path('course/<int:id>/member/', views.member_list_view, name='member_list'),
]
