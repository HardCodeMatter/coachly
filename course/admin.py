from django.contrib import admin
from .models import (
    Course,
    Member,
    Announcement
)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'author', 'is_active', 'is_premium',)
    list_filter = ('name', 'author', 'is_active', 'is_premium',)

    fieldsets = [
        (None, {
            'fields': ('name', 'description',),
        }),
        ('Personal information', {
            'fields': ('author', 'course_code', 'image',),
        }),
        ('Available content', {
            'fields': ('is_premium', 'is_active',),
        }),
    ]

    search_fields = ('name', 'author', 'course_code', 'is_active', 'is_premium',)
    readonly_fields = ('author',)
    ordering = ('-id',)


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ('user', 'course', 'role',)
    list_filter = ('user', 'course', 'role',)

    fieldsets = [
        (None, {
            'fields': ('user', 'course', 'role',),
        }),
    ]

    search_fields = ('user', 'course', 'role',)
    ordering = ('-id',)


@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'author', 'is_limited',)
    list_filter = ('id', 'course', 'author', 'is_limited', 'date_created',)

    fieldsets = [
        (None, {
            'fields': ('course', 'author',),
        }),
        ('Description', {
            'fields': ('announcement',),
        }),
        ('Date and limit', {
            'fields': ('date_created', 'is_limited',),
        }),
    ]

    search_fields = ('id', 'course', 'author', 'is_limited', 'date_created',)
    ordering = ('-id',)
