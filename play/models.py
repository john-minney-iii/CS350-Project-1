from django.db import models

class BlackCard(models.Model):
    card_text = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.card_text

class WhiteCard(models.Model):
    card_text = models.CharField(max_length=100)
    average_rank = models.DecimalField(max_digits=4, decimal_places=2, default=0.00)

    def __str__(self) -> str:
        return self.card_text
