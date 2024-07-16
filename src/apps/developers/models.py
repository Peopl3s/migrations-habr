from django.db import models


class Developer(models.Model):
    title = models.CharField("Артикул", max_length=32)

    class Meta:
        indexes = [models.Index(fields=["title"])]
        verbose_name = "Застройщик"
        verbose_name_plural = "Застройщики"
