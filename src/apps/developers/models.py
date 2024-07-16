from django.db import models


class Developer(models.Model):
    title = models.CharField("Артикул", max_length=32)
    inn = models.CharField(verbose_name="ИНН", max_length=12, blank=True)
    rating = models.FloatField(verbose_name="Рейтинг", default=0.0)

    class Meta:
        indexes = [models.Index(fields=["title"])]
        verbose_name = "Застройщик"
        verbose_name_plural = "Застройщики"
