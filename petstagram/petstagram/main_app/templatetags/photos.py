from django import template

from petstagram.main_app.models import PetPhoto

register = template.Library()


@register.simple_tag()
def has_photo():
    return PetPhoto.objects.count() > 0
