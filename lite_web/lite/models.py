from django.db import models


class Version(models.Model):
    """
    :param name => название программного обеспечения
    :param version => версия программного обеспечения
    """
    name = models.CharField(max_length=64, unique=True)
    version = models.CharField(max_length=32)

    def __str__(self):
        """
        Функция вывода названия и версии программного обеспечения
        :return: строку на подобии json формата
        """
        return f'software: {self.name}\nversion: {self.version}'
