from django.db import models


class First(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'First'
        verbose_name_plural = 'Firsts'

    def __str__(self):
        return self.name


class SecondMultiModel(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Second'
        verbose_name_plural = 'Seconds'
        app_label = 'multibase'
