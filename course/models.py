from django.db import models
from django.utils import timezone
from user.models import User


class Course(models.Model):
    name = models.CharField(('name'), max_length=100)
    description = models.TextField(('description'), max_length=500, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course_code = models.IntegerField(
        ('code'),
        unique=True,
        help_text='Indicates an invitation to the course using a code.'
    )
    image = models.ImageField(('image'), upload_to='course/image/')

    is_premium = models.BooleanField(
        ('premium'),
        default=False,
        help_text='Indicates a premium user who has access to premium features.',
    )
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text='Indicates a user who has an active account.'
    )

    def __str__(self) -> str:
        return f'{self.name}'


class Member(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    
    class Roles(models.TextChoices):
        TEACHER = 'TEACHER', 'Teacher'
        STUDENT = 'STUDENT', 'Student'

    role = models.CharField(
        ('role'),
        max_length=50,
        choices=Roles.choices,
        default=Roles.STUDENT,
    )

    def __str__(self) -> str:
        return f'{self.user} - {self.course}'


class Announcement(models.Model):
    announcement = models.TextField(('announcement'), max_length=1500)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created = models.DateTimeField(('data created'), default=timezone.now)

    is_limited = models.BooleanField(
        ('limited'),
        default=False,
        help_text='Indicates a announcement is limited for commenting.'
    )

    def __str__(self) -> str:
        return f'Announcement {self.pk}'


class Task(models.Model):
    name = models.CharField(('name'), max_length=100)
    description = models.TextField(('description'), max_length=500, blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date_created = models.DateTimeField(('date created'), default=timezone.now)
    date_due = models.DateField(('due date'), blank=True, null=True)
    points = models.IntegerField(('points'), blank=True, null=True)
    
    is_active = models.BooleanField(
        ('active'),
        default=True,
        help_text='Indicates a task that has an active status.'
    )

    def __str__(self) -> str:
        return f'{self.name}'


class Grade(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    grade = models.IntegerField(('grade'), null=True)
    date_assigned = models.DateTimeField(('date assigned'), default=timezone.now)

    def __str__(self) -> str:
        return f'Grade {self.pk}'


class File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    file = models.FileField(('file'), upload_to='course/files/')
    date_attached = models.DateTimeField(('date attached'), default=timezone.now)

    def __str__(self) -> str:
        return f'File {self.pk}'