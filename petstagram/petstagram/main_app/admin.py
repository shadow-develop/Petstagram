from django.contrib import admin

# Register your models here.
from petstagram.main_app.models import Profile, Pet


@admin.register(Profile)
class ProfileRegister(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Pet)
class PetRegister(admin.ModelAdmin):
    list_display = ('name', 'type', 'user_profile')

