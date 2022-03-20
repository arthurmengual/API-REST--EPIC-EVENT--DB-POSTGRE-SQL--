from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = models.User
        fields = ('email', )


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = models.User
        fields = ('email', )


@admin.register(models.User)
class UserAdmin(UserAdmin):
    list_display = ('username', 'role')
    list_filter = ('username',)
    search_fields = ('username', 'role')
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    fieldsets = (
        ('Connection info', {'fields': ('username', 'password')}),
        ('Personal info', {'fields': ('first_name',
         'last_name', 'email', 'role')}), ('Permissions', {'fields': ('is_staff', 'is_superuser', 'is_active')}),
    )

    add_fieldsets = (
        ('New user infos', {
            'classes': ('wide', 'extrapretty'),
            'fields': ('username', 'password1', 'password2', 'email', 'role', 'first_name', 'last_name', 'is_staff', 'is_superuser', 'is_active')}
         ),
    )
