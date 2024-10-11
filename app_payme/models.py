from django.db import models

# Create your models here.
class Balance(models.Model):
    system = "payme"
    user_id = models.CharField(max_length=200)
    transaction_id = models.CharField(max_length=200)
    amount = models.CharField(max_length=200)
    state = models.CharField(max_length=200)

    def __str__(self) -> str:
        return f"{self.user_id} --- {self.amount}"
