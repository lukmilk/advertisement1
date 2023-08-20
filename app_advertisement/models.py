from django.db import models


# Create your models here.
class Advertisement(models.Model):
    title = models.CharField(
        max_length=80,
        verbose_name="Название",
    )

    description = models.TextField(
        verbose_name="Описание"
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Цена"
    )

    auction = models.BooleanField(
        verbose_name="Торг",
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата публикации"
    )

    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата редактирования"
    )

    class Meta:
        db_table = 'advertisement'

    def __str__(self):
        return f'Advertisement(id = {self.id}, title = {self.title}, price = {self.price})'
