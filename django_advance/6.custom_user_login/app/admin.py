from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from . import forms, models

class MyUserAdmin(UserAdmin):
    add_form = forms.UserCreationForm
    form = forms.UserChangeForm
    model = models.User
    list_display = ['username', 'email', 'phone']

admin.site.register(models.User, MyUserAdmin)