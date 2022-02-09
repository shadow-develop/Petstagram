from django.contrib import admin

# Register your models here.
from petstagram.main_app.models import Profile, Pet, PetPhoto


class PetInlineAdmin(admin.StackedInline):
    model = Pet


@admin.register(Profile)
class ProfileRegister(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')
    inlines = (PetInlineAdmin,)


@admin.register(Pet)
class PetRegister(admin.ModelAdmin):
    list_display = ('name', 'type', 'user_profile')


@admin.register(PetPhoto)
class PetPhotoRegister(admin.ModelAdmin):
    pass
