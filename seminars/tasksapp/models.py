from django.db import models
from django.utils import timezone


# Задание №1
# Создайте модель для запоминания бросков монеты: орёл или решка.
# Также запоминайте время броска


class Throws(models.Model):
    res_throws = models.CharField(max_length=5)
    time_throws = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'результат броска - {self.res_throws}, время - {self.time_throws}'

    @staticmethod
    def values():
        res = Throws.objects.order_by('-time_throws')[:5]
        return res

# Задание №3
# Создайте модель Автор. Модель должна содержать
# следующие поля:
# ○ имя до 100 символов
# ○ фамилия до 100 символов
# ○ почта
# ○ биография
# ○ день рождения
# Дополнительно создай пользовательское поле “полное имя”, которое возвращает имя и фамилию.


class FullNameField(models.CharField):
    def __init__(self, name, surname, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fullname = name + surname


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    email = models.EmailField()
    biography = models.TextField(max_length=1000)
    birthday = models.DateField()

    def __str__(self):
        return f'name: {self.name}, surname: {self.s}, email: {self.email}'



