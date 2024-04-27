from django.contrib.auth.models import AbstractBaseUser, AbstractUser
from django.db import models
from users.managers import UserManager
# from phonenumber_field.modelfields import PhoneNumberField
from django.utils.translation import gettext_lazy as _


class UserRoles:
    # закончите enum-класс для пользователя
    pass


class User(AbstractBaseUser):
    # переопределение пользователя.
    # подробности также можно поискать в рекоммендациях к проекту
    pass
