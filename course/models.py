from django.db import models
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
