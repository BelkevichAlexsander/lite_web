from django.db import models


class Version(models.Model):
    """
    :param name => название программного обеспечения
    :param first => первое число версии
    :param second => второе число версии
    :param third => третье число версии
    """
    name = models.CharField(max_length=64, unique=True)
    first = models.PositiveIntegerField(default=0)
    second = models.PositiveIntegerField(default=0)
    third = models.PositiveIntegerField(default=0)

    def __str__(self):
        """
        функция вывода названия и версии программного обеспечения
        :return: строку на подобии json формата
        """
        return f'software: {self.name}\n' \
               f'version: {self.first}.{self.second}.{self.third}'

