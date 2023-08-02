from django.db import models

# Title
# Description
# Price
# Negotiable
# Created
# Last Updated

class Advertisement(models.Model):
    title = models.CharField("Заголовок", max_length=128)
    description = models.TextField("Описание")
    price = models.DecimalField("Цена", max_digits=10, decimal_places=2)
    negotiable = models.BooleanField("Торг", help_text="Уместен ли торг?")
    created = models.DateTimeField("Созданo", auto_now_add=True)
    last_updated = models.DateTimeField("Обновленo", auto_now=True)

    def __str__(self) -> str:
        return f"{self.__class__.__name__}(id={self.pk}, title={self.title}, price={self.price})"
    
    class Meta:
        db_table = "advertisements"