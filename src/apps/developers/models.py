from django.db import models


class Developer(models.Model):
    title = models.CharField("Артикул", max_length=32)

    class Meta:
        verbose_name = "Застройщик"
        verbose_name_plural = "Застройщики"
