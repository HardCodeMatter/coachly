from .models import (
    Course,
    Member,
    Announcement,
    Task
)


def course_create(**kwargs):
    return Course.objects.create(**kwargs)

def course_filter_by_user(user, **kwargs):
    return Member.objects.filter(user=user, **kwargs)

def member_create(**kwargs):
    return Member.objects.create(**kwargs)

def announcement_create(**kwargs):
    return Announcement.objects.create(**kwargs)

def task_create(**kwargs):
    return Task.objects.create(**kwargs)
