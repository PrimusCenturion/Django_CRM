from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

class ZAStreetAddress(models.Model):
    class AddressTypes(models.TextChoices):
        PERSONAL    = "1", "Personal"
        BUSINESS    = "2", "Business"

    address_type        = models.CharField(
                            max_length=2,
                            choices=AddressTypes.choices,
                            default=AddressTypes.PERSONAL,
                            blank = True, 
                            null=True, 
                        )
    number              = models.IntegerField(blank=True, null=True)
    street              = models.CharField(max_length=200, blank=True, null=True)
    apartment_name      = models.CharField(max_length=200, blank=True, null=True)
    apartment_number    = models.IntegerField(blank=True, null=True)
    suburb              = models.CharField(max_length=200, blank=True, null=True)
    city                = models.CharField(max_length=200, blank=True, null=True)
    province            = models.CharField(max_length=200, blank=True, null=True) 
    prospect            = models.ForeignKey(
                            'Lead', 
                            blank = True, 
                            null=True, 
                            on_delete=models.SET_NULL
                        )
    # route = TODO this could possibily contain the google map instructions

    @property
    def full(self):
        props = dict(
            number = self.number,
            apartment_name = self.apartment_name,
            apartment_number = self.apartment_number,
            street = self.street,
            suburb = self.suburb,
            city = self.city,
            province = self.province
        )
        output_string = ""
        for each in props.items():
            if each[1] == None:
                pass
            elif each[0] == "number":
                output_string += str(each[1])
            else:
                output_string += f", {each[1]}"
        
        return output_string
    
    def __str__(self):
        return str(self.full)
    
    class Meta:
        verbose_name = "South African Street Address"
        verbose_name_plural = "South African Street Addresses"


class SocialMediaLink(models.Model):
    class SocialMediaChoices(models.TextChoices):
        # TODO Add more options
        LINKEDIN    = "1", "LinkedIn"
        FACEBOOK    = "2", "Facebook"
        INSTAGRAM   = "3", "Instagram"
        TWITTER     = "4", "Twitter"
        OTHER       = "5", "Other"

    social_media        = models.CharField(
                            max_length=2,
                            choices=SocialMediaChoices.choices,
                            default=SocialMediaChoices.LINKEDIN,
                            blank = True, 
                            null=True, 
                        )
    prospect            = models.ForeignKey(
                            'Lead', 
                            blank = True, 
                            null=True, 
                            on_delete=models.SET_NULL
                        )
    link                = models.URLField(blank=True, null=True)

    def __str__(self):
        return f"{self.prospect}, {self.link}"

class Communication(models.Model):
    class CommunicationType(models.TextChoices):
        PHONE_CALL          = "1", "Phone Call"
        EMAIL               = "2", "Email"
        INSTANT_MESSAGE     = "3", "Instant Message"


    prospect = models.ForeignKey('Lead', blank = True, null=True, on_delete=models.SET_NULL)
    communication_type= models.CharField(
                            max_length=2,
                            choices=CommunicationType.choices,
                            default=CommunicationType.PHONE_CALL,
                            blank = True, 
                            null=True, 
                        )
    notes = models.TextField(null=True, blank=True)  

class Lead(models.Model):

    # Personal Information
    class Month(models.TextChoices):
        MR      = "1", "Mr"
        MRS     = "2", "Mrs"
        MISS    = "3", "Miss"
        MS      = "4", "Ms"
        DR      = "5", "Dr"
        PROF    = "6", "Prof"

    first_name              = models.CharField(max_length=200)
    last_name               = models.CharField(max_length=200)

    title                   = models.CharField(
                                max_length=2,
                                choices=Month.choices,
                                default=Month.MR,
                                blank=True,
                                null=True
                            )

    email                   = models.EmailField(blank=True, null=True)
    phone_number            = PhoneNumberField(blank=True, null=True)
    mobile_number           = PhoneNumberField(blank=True, null=True)
    personal_website        = models.URLField(blank=True, null=True)

    # Company Information
    job_title               = models.CharField(max_length=200, blank=True, null=True)
    company_name            = models.CharField(max_length=200, blank=True, null=True)
    company_website         = models.URLField(blank=True, null=True)
    company_number          = PhoneNumberField(blank=True, null=True)

    # Social Media Links
    social_media_links      = models.ManyToManyField(SocialMediaLink)

    # Addresses
    address                 = models.ManyToManyField(ZAStreetAddress)

    # Communications Preferences
    communications          = models.ManyToManyField(Communication)

    def __str__(self):
        return f"{self.first_name}, {self.last_name}".upper()

