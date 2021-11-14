from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import fields
from .models import User
from django.contrib.auth.forms import UserChangeForm

class UserAdminForm(UserChangeForm):
    class Meta:
        fields='__all__'

class CustomUserAdmin(UserAdmin):
    form= UserAdminForm
    list_display = ('username','first_name','last_name','is_staff','mobile',)
    fieldset={
        ''
    }
    
admin.site.register(User,CustomUserAdmin)