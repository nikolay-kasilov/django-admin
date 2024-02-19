from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from userprofiles.models import User, Profile


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    readonly_fields = ('date_joined', 'last_login')
    list_display = ('id', 'username')
    fieldsets = (
        (None, {'fields': ('username',)}),
        ('Персональная информация',
         {'fields': ('first_name', 'last_name', 'email')}),
        ('Разрешения', {'fields': ('is_active', 'is_staff')}),
        ('Даты', {'fields': ('last_login', 'date_joined')})
    )


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('id', 'title')
    search_fields = ('title',)
    fieldsets = [
        ('Название', {'fields': ('title',)}),
    ]


admin.site.unregister(Group)
