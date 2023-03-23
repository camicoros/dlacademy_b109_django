from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from .validators import validate_birth_date


class CustomUser(AbstractUser):
    birth_date = models.DateField(_('birth date'), blank=True, null=True, validators=[validate_birth_date])
    about = models.TextField(max_length=1000, blank=True)
    avatar = models.ImageField(upload_to="profile")
    friends = models.ManyToManyField('self', blank=True)
    phone_number = models.CharField(max_length=11, blank=True, null=True)

    def __str__(self):
        return str(self.username)
