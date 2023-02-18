from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserChangeForm, UserCreationForm
from .models import Role, User

admin.site.unregister(Group)


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('name', 'level',)
    list_filter = ('name', 'level',)

    fieldsets = (
        (None, {'fields': ('name', 'level',)}),
        ('Permissions', {'fields': ('permissions',)}),
    )

    search_fields = ('name', 'level',)
    ordering = ('level',)
    filter_horizontal = ('permissions',)


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('__str__', 'email', 'role',)
    list_filter = ('first_name', 'last_name', 'email',)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': (
            'first_name',
            'last_name',
        )}),
        ('Permissions', {'fields': (
            'date_joined',
            'is_staff',
            'is_active',
            'is_verified',
            'role',
        )}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )
    search_fields = ('first_name', 'last_name', 'email')
    ordering = ('id',)
    filter_horizontal = ()
