from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class SocialMediaLink(models.Model):
    class SocialMediaChoices(models.TextChoices):
        # TODO Add more options
        LINKEDIN    = "1", "LinkedIn"
        FACEBOOK    = "2", "Facebook"
        INSTAGRAM   = "3", "Instagram"
        TWITTER     = "4", "Twitter"
        OTHER       = "5", "Other"

    social_media = models.CharField(
        max_length=2,
        choices=SocialMediaChoices.choices,
        default=SocialMediaChoices.LINKEDIN,
        blank = True, 
        null=True, 
    )
    prospect = models.ForeignKey(
        'Lead', 
        blank = True, 
        null=True, 
        on_delete=models.SET_NULL
        )
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.prospect}, {self.link}"

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
        default=Month.MR,
        blank=True,
        null=True
    )

    email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    mobile_number = PhoneNumberField(blank=True, null=True)

    social_media_links = models.ManyToManyField(SocialMediaLink) 

    def __str__(self):
        return f"{self.first_name}, {self.last_name}".upper()

