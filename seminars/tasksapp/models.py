from django.db import models


# Задание №1
# Создайте модель для запоминания бросков монеты: орёл или решка.
# Также запоминайте время броска

class Throws(models.Model):
    res_throws = models.CharField(max_length=5)
    time_throws = models.DateTimeField()

    def __str__(self):
        return f'результат броска - {self.res_throws}, время - {self.time_throws}'
