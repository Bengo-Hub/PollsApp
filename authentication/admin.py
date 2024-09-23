from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    # Define the fields to be used in displaying the CustomUser model
    list_display = ('id_no', 'gender', 'is_active', 'is_staff', 'is_superuser')
    list_filter = ('is_active', 'is_staff', 'is_superuser')
    ordering = ('id_no',)
    search_fields = ('id_no',)
    
    # Define the fields for the user creation and update forms
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('id_no', 'gender', 'password1', 'password2', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
    
    fieldsets = (
        (None, {
            'fields': ('id_no', 'gender', 'password', 'is_active', 'is_staff', 'is_superuser')}
        ),
    )
