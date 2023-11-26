from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class Lead(models.Model):
    class Month(models.TextChoices):
        MR      = "1", "Mr"
        MRS     = "2", "Mrs"
        MISS    = "3", "Miss"
        MS      = "4", "Ms"
        DR      = "5", "Dr"
        PROF    = "6", "Prof"

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    title = models.CharField(
        max_length=2,
        choices=Month.choices,
        default=Month.MR
    )

    # email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.first_name
