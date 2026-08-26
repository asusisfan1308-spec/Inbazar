from django.db import models


class BranchLocation(models.Model):
    name = models.CharField(max_length=150, verbose_name="Название филиала")
    address = models.CharField(max_length=255, verbose_name="Адрес локации")
    landmark = models.CharField(max_length=255, blank=True, null=True, verbose_name="Ориентир")
    map_link = models.URLField(max_length=500, verbose_name="Ссылка на карту (Yandex/Google Maps)")
    photo = models.ImageField(upload_to='branches/photos/', verbose_name="Фотография филиала")

    class Meta:
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"
        ordering = ['name']

    def __str__(self):
        return f"{self.name} ({self.address})"


