from django.contrib import admin

# Register your models here.
from petstagram.main_app.models import Profile


@admin.register(Profile)
class ProfileRegister(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'date_of_birth')

