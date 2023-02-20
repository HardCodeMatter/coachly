from .models import Course


def course_create(**kwargs):
    return Course.objects.create(**kwargs)
