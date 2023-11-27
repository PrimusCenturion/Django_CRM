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

    email = models.EmailField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True)
    mobile_number = PhoneNumberField(blank=True, null=True)

    def __str__(self):
        return self.first_name

# TODO Add Fields

# Mobile Number

# Social Media Profiles:
# LinkedIn Profile
# Twitter Handle
# Facebook Profile
# Instagram Handle
# Professional Information:

# Job Title
# Company Name
# Work Address
# Preference for Email, Phone, or In-person communication

# Mailing Address:
# Home Address or Business Address
# Website:

# Personal or Company Website URL
# Fax Number:

# Time Zone Information:

# Preferred language for communication
# Assistant or Secretary Contact:

# Alternate Contact Information:

# Secondary email address
# Alternative phone number

# Preferred Contact Time:

# Ideal times for communication
# Callback Preferences:

# Whether the lead prefers callbacks and the preferred time
# Notification Preferences:

# Preferences for receiving notifications or updates
# Emergency Contact Information:

# If applicable and necessary
# Preferred Method for Urgent Communication:

# Whether the lead prefers urgent communication via phone, email, or another channel
# Spouse or Family Contact Information:

# Preferred Contact Frequency:

# Callback Availability:

# Days and times when the lead is available for callback

# Callback Notes:

# Any specific notes or preferences related to callbacks
# Third-Party Communication Preferences:

# Preferences for third-party communication, if applicable
# Preferred Contact Method for Updates:

# How the lead prefers to receive updates (email, phone, etc.)  

# Notes