from django.db import models


class Flat(models.Model):
    article = models.CharField("Артикул", max_length=32)
    area = models.FloatField("Площадь",)
    price = models.IntegerField("Цена", default=0, blank=True)

    developer = models.ForeignKey(
        'developers.Developer',
        verbose_name="Застройщик",
        related_name='flats',
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    class Meta:
        indexes = [models.Index(fields=["article"])]
        verbose_name = "Квартира"
        verbose_name_plural = "Квартиры"
