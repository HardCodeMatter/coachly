from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Permission
from .manager import UserManager
from django.utils import timezone


class Role(models.Model):
    name = models.CharField(('name'), max_length=100)
    level = models.IntegerField(('level'))
    permissions = models.ManyToManyField(Permission, related_name='permissions')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name = 'Role'
        verbose_name_plural = 'Roles'


class User(AbstractBaseUser, PermissionsMixin):
    username = None
    email = models.EmailField(('email address'), unique=True, max_length=150)
    
    first_name = models.CharField(('first name'), max_length=30)
    last_name = models.CharField(('last name'), max_length=30)
    
    date_joined = models.DateTimeField(('date joined'), default=timezone.now)
    is_staff = models.BooleanField(('staff'), default=False)
    is_active = models.BooleanField(('active'), default=True)
    is_verified = models.BooleanField(('verified'), default=False)

    role = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [
        'first_name', 'last_name',
    ]

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def get_full_name(self):
        return f'{self.first_name} {self.last_name}'

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    @property
    def is_admin(self):
        "Is the user an admin member?"
        return self.is_staff
