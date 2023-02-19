from django.contrib import admin
from .models import Course


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
