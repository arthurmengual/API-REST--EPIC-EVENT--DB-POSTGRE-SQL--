from django.contrib import admin
from . import models
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm):
#         model = models.User
#         fields = ('email', )


# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = models.User
#         fields = ('email', )


# @admin.register(models.User)
# class UserAdmin(UserAdmin):
#     list_display = ('username', 'role')
#     list_filter = ('username',)
#     search_fields = ('username', 'role')
#     add_form = CustomUserCreationForm
#     form = CustomUserChangeForm
#     fieldsets = (
#         (None, {'fields': ('email', 'password')}),
#         ('Personal info', {'fields': ('username', 'first_name',
#          'last_name', 'role', 'is_staff', 'is_superuser', 'is_active')}),
#     )
#     # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
#     # overrides get_fieldsets to use this attribute when creating a user.
#     add_fieldsets = (
#         (None, {
#             'classes': ('wide',),
#             'fields': ('username', 'password1', 'password2', 'is_staff', 'is_superuser', 'is_active', 'first_name', 'last_name', 'email', 'role')}
#          ),
#     )


@admin.register(models.Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('status', 'first_name', 'last_name')
    list_filter = ['status']
    search_fields = ('status', 'last_name', 'support_contact', 'sales_contact')


@admin.register(models.Contract)
class ContractAdmin(admin.ModelAdmin):
    list_display = ('client', 'date_created', 'support_contact', 'sales_contact')
    list_filter = ['date_created']
    search_fields = ('client', 'date_created', 'support_contact', 'sales_contact')


@admin.register(models.Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('client', 'date', 'support_contact', 'sales_contact')
    search_fields = ('client', 'date', 'support_contact', 'sales_contact')


admin.site.register(models.EventStatu)
