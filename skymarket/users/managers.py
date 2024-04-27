from django.contrib.auth.models import (
    BaseUserManager
)
# здесь должен быть менеджер для модели Юзера.
# Поищите эту информацию в рекомендациях к проекту
class UserManager(BaseUserManager):
    pass
