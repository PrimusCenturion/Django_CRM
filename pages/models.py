from django.db import models

class CookiePreferences(models.Model):
    accept_cookies = models.BooleanField()
