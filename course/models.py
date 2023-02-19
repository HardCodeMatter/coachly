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

    def __str__(self):
        return f'{self.name}'
