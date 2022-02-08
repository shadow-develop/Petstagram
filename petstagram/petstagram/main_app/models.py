from django.core.validators import MinLengthValidator
from django.db import models

# Create your models here.
from petstagram.main_app.validators import validate_only_letters, validate_file_max_size_in_mb


class Profile(models.Model):
    FIRST_NAME_MAX_LENGTH = 30
    FIRST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2

    GENDERS = [
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Do Not Show', 'Do Not Show'),
    ]

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validate_only_letters,
        )
    )

    picture = models.URLField()

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    email = models.EmailField(
        null=True,
        blank=True,
    )

    gender = models.CharField(
        max_length=max([len(x) for x, _ in GENDERS]),
        choices=[(x, x) for _, x in GENDERS],
    )

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Pet(models.Model):
    NAME_MAX_LENGTH = 30

    TYPES = [
        ('Cat', 'Cat'),
        ('Dog', 'Dog'),
        ('Bunny', 'Bunny'),
        ('Parrot', 'Parrot'),
        ('Fish', 'Fish'),
        ('Other', 'Other'),
    ]

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
    )

    type = models.CharField(
        max_length=max([len(x) for x, _ in TYPES]),
        choices=[(x, x) for _, x in TYPES],
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True,
    )

    user_profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} the {self.type}'

    class Meta:
        unique_together = ('user_profile', 'name')


class PetPhoto(models.Model):
    photo = models.ImageField(
        validators=(
            # validate_file_max_size_in_mb(5),
        )
    )

    tagged_pets = models.ManyToManyField(
        Pet,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        auto_now_add=True
    )

    likes = models.IntegerField(
        default=0
    )